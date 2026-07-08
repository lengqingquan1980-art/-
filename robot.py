import requests
import re
from urllib.parse import unquote


# =========================
# 频道地址
# =========================

CHANNEL = "https://www.youtube.com/@SFZY666/videos"


headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
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
# 读取视频页面
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



# =========================
# 搜索关键词
# =========================


keyword = "最新免费节点获取地址"


pos = video_html.find(keyword)



if pos == -1:

    print()
    print("没有找到关键词")

    exit()



print()
print("找到关键词！")



# 取附近内容

part = video_html[
    pos:
    pos + 2000
]



print()
print("开始解析网址...")



# =========================
# 提取网址
# =========================


urls = re.findall(
    r'https?://[^\s"\\<>]+',
    part
)



results = []



for u in urls:


    u = unquote(u)


    u = u.replace(
        "\\u0026",
        "&"
    )


    u = u.replace(
        "\\/",
        "/"
    )


    if "skill-note.blogspot.com" in u:

        results.append(u)



# 去重

final = []


for u in results:

    if u not in final:

        final.append(u)



print()
print("找到真实网址数量:")
print(len(final))



for i,u in enumerate(final,1):

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


    for u in final:

        f.write(
            u + "\n"
        )



print()
print("完成")
print("已保存 links.txt")
