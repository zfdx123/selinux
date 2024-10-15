def remove_duplicates(input_file, output_file):
    # 使用集合存储唯一的权限条目
    unique_permissions = set()
    
    # 读取输入文件
    with open(input_file, 'r') as file:
        for line in file:
            # 去除首尾空白并只处理非空行
            stripped_line = line.strip()
            if stripped_line:
                unique_permissions.add(stripped_line)

    # 将唯一的条目写入输出文件
    with open(output_file, 'w') as file:
        for permission in sorted(unique_permissions):
            file.write(f"{permission}\n")

# 使用示例
input_file_path = 'rule_magisk.rule'  # 输入文件路径
output_file_path = 'new_rule_magisk.rule'  # 输出文件路径

remove_duplicates(input_file_path, output_file_path)
print(f"去重完成，结果已写入 {output_file_path}。")
