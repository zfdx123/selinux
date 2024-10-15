import re

class SELinuxRuleGenerator:
    def __init__(self, log_file_path):
        # 初始化日志文件路径
        self.log_file_path = log_file_path
        self.linux_rules = set()   # 用于存储Linux格式的规则
        self.magisk_rules = set()  # 用于存储Magisk格式的规则

    def __read_dmesg_log(self):
        # 读取日志文件内容
        with open(self.log_file_path, 'r') as file:
            logs = file.read()
        return logs

    def __parse_dmesg_for_selinux(self, logs):
        # 解析出 SELinux 相关日志，生成 allow 规则
        pattern = (r"avc:  denied  \{ (\w+) \} for .*"
                   r"scontext=([^ ]+) .*"
                   r"tcontext=([^ ]+) .*"
                   r"tclass=(\w+)")
        
        for line in logs.splitlines():
            match = re.search(pattern, line)
            if match:
                permission = match.group(1)  # 操作权限 (e.g., read, write)
                source_context = match.group(2)  # 源上下文 (e.g., httpd_t)
                target_context = match.group(3)  # 目标上下文 (e.g., var_log_t)
                tclass = match.group(4)  # 类 (e.g., file)

                # 提取类型（即上下文的第三部分），忽略 SELinux 用户和角色
                source_type = source_context.split(":")[2]
                target_type = target_context.split(":")[2]

                # 生成规则并存储到集合中，自动去重
                self.linux_rules.add(f"allow {source_type} {target_type}:{tclass} {permission};")
                self.magisk_rules.add(f"allow {source_type} {target_type} {tclass} {permission}")

    def __write_rule(self):
        # 将规则写入文件
        with open("rule_linux.rule", 'w+') as f:
            for rule in self.linux_rules:
                f.write(f"{rule}\n")
                print(rule)

        with open("rule_magisk.rule", 'w+') as f:
            for rule in self.magisk_rules:
                f.write(f"{rule}\n")

    def generate_selinux_allow_rules(self):
        # 读取并解析日志文件，生成 SELinux 规则
        logs = self.__read_dmesg_log()
        self.__parse_dmesg_for_selinux(logs)
        if self.linux_rules:
            print("生成SELinux允许规则:")
            self.__write_rule()
        else:
            print("没有找到匹配的SELinux日志!")

if __name__ == "__main__":
    # 替换为你的日志文件路径
    log_file_path = "./1_selinux.txt"
    rule_generator = SELinuxRuleGenerator(log_file_path)
    rule_generator.generate_selinux_allow_rules()
    
