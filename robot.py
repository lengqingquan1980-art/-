import requests
import re
from urllib.parse import urlparse, parse_qs, unquote

CHANNEL = "https://www.youtube.com/@SFZY666/videos"

headers = {
    "User-Agent": "Mozilla/5.0"
}

print("========== 获取频道 ==========")

html = requests.get(
    CHANNEL,
    headers=headers,
    timeout=20
).text

# ----------------------------
# 获取视频ID
# ----------------------------

video_ids = re.findall(
    r'"videoId":"([a-zA-Z0-9_-]{11})"',
    html
)

unique = []

for v in video_ids:
    if v not in unique:
        unique.append(v)

if not unique:
    print("没有找到任何视频")
    exit()

print("找到视频数量：", len(unique))

latest = unique[0]

video_url = f"https://www.youtube.com/watch?v={latest}"

print()
print("最新视频：")
print(video_url)

# ----------------------------
# 获取视频页面
# ----------------------------

print()
print("========== 获取视频页面 ==========")

video_html = requests.get(
    video_url,
    headers=headers,
    timeout=20
).text

# ----------------------------
# 解析简介
# ----------------------------

print("正在解析简介...")

m = re.search(
    r'"shortDescription":"(.*?)","isCrawlable"',
    video_html,
    re.S
)

if not m:
    print("没有找到简介")
    exit()

desc = m.group(1)

# Unicode转义
desc = desc.encode().decode("unicode_escape")

# 去掉JSON里的转义
desc = desc.replace("\\/", "/")

print()
print("========== 视频简介 ==========")
print(desc)

# ----------------------------
# 提取网址
# ----------------------------

print()
print("========== 提取网址 ==========")

urls = re.findall(
    r'https?://[^\s]+',
    desc
)

if not urls:
    print("简介中没有网址")
    exit()

print("找到网址：")

for i, u in enumerate(urls, 1):
    print(i, u)

# ----------------------------
# 解析YouTube Redirect
# ----------------------------

print()
print("========== 解析真实网址 ==========")

real_urls = []

for u in urls:

    if "youtube.com/redirect" in u:

        parsed = urlparse(u)

        params = parse_qs(parsed.query)

        if "q" in params:

            real = unquote(params["q"][0])

            real_urls.append(real)

            print("Redirect ->", real)

        else:
            real_urls.append(u)

    else:
        real_urls.append(u)

# 去重
real_urls = list(dict.fromkeys(real_urls))

# ----------------------------
# 跟踪跳转
# ----------------------------

print()
print("========== 跟踪302跳转 ==========")

final_urls = []

for u in real_urls:

    try:

        r = requests.get(
            u,
            headers=headers,
            allow_redirects=True,
            timeout=20
        )

        print()
        print("原始：", u)
        print("最终：", r.url)

        final_urls.append(r.url)

    except Exception as e:

        print("失败：", u)
        print(e)

# 去重
final_urls = list(dict.fromkeys(final_urls))

# ----------------------------
# 保存
# ----------------------------

with open(
    "links.txt",
    "w",
    encoding="utf-8"
) as f:

    for u in final_urls:
        f.write(u + "\n")

print()
print("========== 完成 ==========")
print("共保存", len(final_urls), "个链接")
print("已写入 links.txt")
