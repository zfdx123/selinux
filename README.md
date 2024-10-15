# selinux
根据Linux日志(dmesg)生成SELinux Allow规则

## generate_rule.py
根据生成的日志生成规则，修改代码中 [log_file_path = "./1_selinux.txt"](https://github.com/zfdx123/selinux/blob/master/generate_rule.py#L62) 为自己日志文件的路径和名称
修改下面可以修改保存文件的名称
[rule_linux](https://github.com/zfdx123/selinux/blob/master/generate_rule.py#L41)
[rule_magisk](https://github.com/zfdx123/selinux/blob/master/generate_rule.py#L46)

## remove_rule_repeat.py
修改示例文件中的输入输出文件即可
