import requests
import re
from urllib.parse import urlparse, parse_qs, unquote


# =========================
# 配置
# =========================

CHANNEL = "https://www.youtube.com/@SFZY666/videos"

KEYWORD = "最新免费节点获取地址"


headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 "
    "(KHTML, like Gecko) "
    "Chrome/120.0 Safari/537.36"
}


# =========================
# 获取最新视频
# =========================

print("正在获取频道页面...")


html = requests.get(
    CHANNEL,
    headers=headers,
    timeout=20
).text


video_ids = re.findall(
    r'"videoId":"([a-zA-Z0-9_-]{11})"',
    html
)


unique = []

for vid in video_ids:

    if vid not in unique:
        unique.append(vid)



print("找到视频数量:", len(unique))


if len(unique) == 0:

    print("没有找到视频")

    exit()



latest = unique[0]


print()
print("最新视频ID:")
print(latest)



video_url = (
    "https://www.youtube.com/watch?v="
    + latest
)


print()
print("视频地址:")
print(video_url)



# =========================
# 获取视频页面
# =========================

print()
print("正在读取视频介绍...")


video_html = requests.get(
    video_url,
    headers=headers,
    timeout=20
).text


print()
print("页面长度:")
print(len(video_html))



pos = video_html.find(KEYWORD)


if pos == -1:

    print()
    print("没有找到关键词")

    exit()



print()
print("找到关键词!")



# 只看关键词附近
part = video_html[
    pos:
    pos + 5000
]



print()
print("正在解析网址...")



# =========================
# 找 youtube redirect
# =========================

redirects = re.findall(
    r'https://www\.youtube\.com/redirect\?[^"]+',
    part
)



real_urls = []



for url in redirects:


    # 修复转义

    url = url.replace(
        "\\u0026",
        "&"
    )


    parsed = urlparse(url)


    params = parse_qs(
        parsed.query
    )


    if "q" in params:


        real = unquote(
            params["q"][0]
        )


        real = real.replace(
            "\\/",
            "/"
        )


        # ★关键修复
        # 删除 YouTube 自己的 v 参数

        real = real.split(
            "&v="
        )[0]


        real_urls.append(real)




print()
print("找到真实网址数量:")
print(len(real_urls))



for i,u in enumerate(real_urls,1):

    print(
        i,
        u
    )



# =========================
# 保存
# =========================


with open(
    "links.txt",
    "w",
    encoding="utf-8"
) as f:


    for u in real_urls:

        f.write(
            u + "\n"
        )



print()
print("完成")
print("已保存 links.txt")
