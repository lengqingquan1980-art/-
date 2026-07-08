import requests
import re
from urllib.parse import unquote


# =========================
# 配置
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



# =========================
# 查找关键词
# =========================


keyword = "最新免费节点获取地址"


pos = video_html.find(keyword)



if pos == -1:

    print()
    print("没有找到关键词")

    exit()



print()
print("找到关键词！")



# =========================
# 搜索完整网址
# =========================


print()
print("正在搜索完整网址...")



# 处理 YouTube 转义

clean_html = video_html.replace(
    "\\/",
    "/"
)


clean_html = clean_html.replace(
    "\\u0026",
    "&"
)



urls = re.findall(
    r'https?://skill-note\.blogspot\.com/[a-zA-Z0-9_/?=&%.\-]+',
    clean_html
)



# 去重

results = []


for u in urls:

    u = unquote(u)

    if u not in results:

        results.append(u)



print()
print("找到网址数量:")
print(len(results))



for i,u in enumerate(results,1):

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

    for u in results:

        f.write(
            u + "\n"
        )



print()
print("完成")
print("已保存 links.txt")
