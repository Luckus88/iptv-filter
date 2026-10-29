#!/usr/bin/env python3
# iptv-filter：m3u IPTV频道过滤工具
import sys

def filter_m3u(input_file, output_file, keep_keywords):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    result = []
    keep_next = False
    for line in lines:
        line_strip = line.strip()
        if line_strip.startswith('#EXTINF:'):
            keep_next = any(k in line for k in keep_keywords)
            if keep_next:
                result.append(line)
        elif line_strip.startswith('http') and keep_next:
            result.append(line)
            keep_next = False
        elif '#EXTM3U' in line:
            result.append(line)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(result)

if __name__ == "__main__":
    # =========在这里修改你想要保留的频道关键词=========
    KEEP_KEYWORDS = ["CCTV", "湖南卫视", "浙江卫视", "江苏卫视"]
    if len(sys.argv) < 3:
        print("使用方法：python filter.py input.m3u output.m3u")
        sys.exit(1)
    filter_m3u(sys.argv[1], sys.argv[2], KEEP_KEYWORDS)
