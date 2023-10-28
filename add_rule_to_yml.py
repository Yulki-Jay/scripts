# 在这里定义一下file path，然后运行这个脚本就可以了
file_path = "C:\\Users\\jiang\\.config\\clash\\profiles\\1698237974614.yml"


# 保存着所有追加的规则
content_to_append = [
    "  - DOMAIN-SUFFIX,jlu.edu.cn,🎯 全球直连",
    "  - DOMAIN-SUFFIX,claude.ai,🇺🇲 美国节点",
    "  - DOMAIN-KEYWORD,emby,🇭🇰 香港节点",
    "  - DOMAIN-SUFFIX,anthropic.com,🇺🇲 美国节点",
    "  - IP-CIDR,139.220.243.0/24,🎯 全球直连,no-resolve",
    "  - IP-CIDR,222.27.87.0/24,🎯 全球直连,no-resolve",
    "  - DOMAIN-SUFFIX,yulki.fun,🇭🇰 香港节点",
    "  - DOMAIN-SUFFIX,yulki.tech,🇭🇰 香港节点",
    "  - DOMAIN-SUFFIX,yulki.codes,🇭🇰 香港节点",
    "  - MATCH,🐟 漏网之鱼",
]


# 打开文件以追加内容
with open(file_path, "r",encoding='utf-8') as file:
    lines = file.readlines()
    if lines:
        lines.pop()
        with open(file_path,'w',encoding='utf-8') as file1:
            file1.writelines(lines)
            for line in content_to_append:
                file1.write(line + "\n")
    # for line in content_to_append:
    #     file.write(line + "\n")
        
print("内容已成功追加到文件中。")
