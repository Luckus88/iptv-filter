# iptv-filter
简单的 IPTV m3u 直播源过滤脚本，支持按频道关键词白名单筛选频道，剔除不需要的频道。

## 运行环境
Python3

## 使用教程
1. 准备原始直播源文件，命名为 `input.m3u`
2. 修改 `filter.py` 里 `KEEP_KEYWORDS`，填入你想保留的频道名称关键词
3. 执行脚本
```bash
python filter.py input.m3u output.m3u
