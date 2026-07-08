import requests
import re
import json
import os
from urllib.parse import urlparse, parse_qs, unquote

# 频道地址
CHANNEL = "https://www.youtube.com/@SFZY666/videos"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

try:
    print("正在获取频道页面...")
    resp_channel = requests.get(CHANNEL, headers=headers, timeout=10)
    html = resp_channel.text

    # 提取所有videoId
    video_ids = re.findall(r'"videoId":"([a-zA-Z0-9_-]{11})"', html)
    # 去重
    unique_video_ids = []
    for vid in video_ids:
        if vid not in unique_video_ids:
            unique_video_ids.append(vid)

    if not unique_video_ids:
        print("未抓取到任何视频ID，YouTube页面动态加载，普通requests无法完整获取数据！")
        exit(1)

    print("找到视频数量:", len(unique_video_ids))
    latest_vid = unique_video_ids[0]
    video_url = f"https://www.youtube.com/watch?v={latest_vid}"
    print(f"\n最新视频ID：{latest_vid}")
    print(f"视频地址：{video_url}")

    # 请求视频详情页
    print("\n正在读取视频介绍...")
    resp_video = requests.get(video_url, headers=headers, timeout=10)
    video_html = resp_video.text
    print(f"页面长度：{len(video_html)}")

    keyword = "最新免费节点获取地址"
    pos = video_html.find(keyword)
    if pos == -1:
        print("\n没有找到关键词")
        exit(0)
    print("\n找到关键词！")

    # 截取关键词后3000字符
    content_part = video_html[pos:pos + 10000]
    # 正则提取页面内所有http/https链接（修复缺失urls变量）
    urls = re.findall(r'https?://[^\s"\']+', content_part)
    if not urls:
        print("关键词附近未找到任何链接")
        exit(0)

    # 解析youtube跳转链接
    real_urls = []
    for u in urls:
        if "youtube.com/redirect" in u:
            parsed = urlparse(u)
            params = parse_qs(parsed.query)
            if "q" in params:
                real_link = unquote(params["q"][0])

                real_link = real_link.replace(
                    "\\u0026",
                    "&"
                )

                real_link = real_link.replace(
                    "\\/",
                    "/"
                )

                real_urls.append(real_link)
        else:
            real_urls.append(u)

    # 输出解析后的中转链接
    print("\n解析后原始网址：")
    for idx, link in enumerate(real_urls, 1):
        print(f"{idx}. {link}")

    # 跟随重定向获取最终真实地址
    final_urls = []
    print("\n开始跟踪短链接跳转...")
    for link in real_urls:
        try:
            resp = requests.get(link, headers=headers, allow_redirects=True, timeout=15)
            print(f"跳转至：{resp.url}")
            final_urls.append(resp.url)
        except Exception as err:
            print(f"链接访问失败 {link}，错误：{str(err)}")

    # 写入文件
    with open("links.txt", "w", encoding="utf-8") as f:
        for link in final_urls:
            f.write(link + "\n")
    print("\n所有最终链接已保存至 links.txt")

except requests.exceptions.Timeout:
    print("请求超时：国内网络无法直连YouTube，需要合规境外网络环境")
except requests.exceptions.ConnectionError:
    print("连接失败：无法访问YouTube域名")
except Exception as e:
    print(f"程序异常：{str(e)}")
