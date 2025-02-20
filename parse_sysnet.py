#!/usr/bin/env python3
import sys
import os

def strip_prefixes(line):
    """
    去掉行首的 'TcpExt: ' 或 'IpExt: ' 等前缀，返回后面纯字段或数值。
    """
    line = line.strip()
    prefixes = ["TcpExt: ", "IpExt: "]
    for p in prefixes:
        if line.startswith(p):
            return line[len(p):]  # 去掉前缀
    return line

def main(file_path):
    if not os.path.isfile(file_path):
        print(f"Error: file '{file_path}' does not exist.")
        sys.exit(1)
    
    lines = []
    # 读取文件全部内容
    with open(file_path, 'r', encoding='utf-8') as f:
        for raw_line in f:
            line = raw_line.strip()
            # 跳过空行
            if not line:
                continue
            # 去掉前缀并按空格切分
            fields_or_vals = strip_prefixes(line).split()
            lines.append(fields_or_vals)

    # 两行一组
    # 假设是成对出现：第一行字段，第二行数值
    for i in range(0, len(lines), 2):
        if i + 1 >= len(lines):
            break  # 保证不会越界
        
        fields = lines[i]
        values = lines[i+1]
        
        # 如果字段数跟数值数不匹配，跳过
        if len(fields) != len(values):
            continue
        
        # 过滤掉数值为 "0" 的列
        pairs = []
        for field, val in zip(fields, values):
            if val != "0":
                pairs.append((field, val))
        
        # 如果此组里所有数值都是 0，则 pairs 为空，跳过
        if not pairs:
            continue

        # 计算字段列的最大宽度，用于对齐
        max_field_len = max(len(p[0]) for p in pairs)

        # 打印非零结果
        for field, val in pairs:
            print(f"{field:<{max_field_len}}  {val}")
        
        # 组与组之间空一行
        print()

if __name__ == "__main__":
    # 脚本用法: python parse_tcp_stats.py stats.txt
    if len(sys.argv) < 2:
        print("Usage: python parse_tcp_stats.py <stats_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    main(file_path)
