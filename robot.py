import requests
import re
from urllib.parse import unquote


CHANNEL = "https://www.youtube.com/@SFZY666/videos"


headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}


print("正在获取频道页面...")


html = requests.get(
    CHANNEL,
    headers=headers,
    timeout=20
).text



# 找视频ID

video_ids = re.findall(
    r'"videoId":"([a-zA-Z0-9_-]{11})"',
    html
)



unique = []


for vid in video_ids:

    if vid not in unique:

        unique.append(vid)



print("找到视频数量:", len(unique))


if not unique:

    print("没有找到视频")

    exit()



latest = unique[0]


video_url = (
    "https://www.youtube.com/watch?v="
    + latest
)



print()
print("最新视频ID:")
print(latest)


print()
print("视频地址:")
print(video_url)



# 获取视频页面

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



keyword = "最新免费节点获取地址"


pos = video_html.find(keyword)



if pos == -1:

    print("没有找到关键词")

    exit()



print()
print("找到关键词！")



# =========================
# 调试附近源码
# =========================


print()
print("=====关键词附近源码=====")


near = video_html[
    pos:
    pos + 10000
]


print(near)


print("=====源码结束=====")



# =========================
# 清理转义
# =========================


clean = video_html


clean = clean.replace(
    "\\/",
    "/"
)


clean = clean.replace(
    "\\u0026",
    "&"
)



clean = unquote(clean)



# =========================
# 查找完整网址
# =========================


print()
print("正在搜索完整地址...")


urls = re.findall(
    r'https?://skill-note\.blogspot\.com/[^\s"<>\\]+',
    clean
)



results = []


for u in urls:

    if "..." not in u:

        if u not in results:

            results.append(u)



print()
print("找到完整网址数量:")
print(len(results))



for i,u in enumerate(results,1):

    print(
        i,
        u
    )



# 保存

with open(
    "links.txt",
    "w",
    encoding="utf-8"
) as f:

    for u in results:

        f.write(
            u+"\n"
        )



print()
print("完成")
print("已保存 links.txt")
