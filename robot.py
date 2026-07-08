import requests
import re
import json
import os


CHANNEL = "https://www.youtube.com/@SFZY666/videos"


headers = {
    "User-Agent": "Mozilla/5.0"
}


print("正在获取频道页面...")


html = requests.get(
    CHANNEL,
    headers=headers
).text



# 找视频ID

video_ids = re.findall(
    r'"videoId":"([a-zA-Z0-9_-]{11})"',
    html
)


unique = []

for v in video_ids:
    if v not in unique:
        unique.append(v)



print("找到视频数量:", len(unique))


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



print()
print("正在读取视频介绍...")


video_html = requests.get(
    video_url,
    headers=headers
).text



print()
print("页面长度:")
print(len(video_html))



keyword = "最新免费节点获取地址"


pos = video_html.find(keyword)



if pos == -1:

    print()
    print("没有找到关键词")

    exit()



print()
print("找到关键词！")



# 取关键词附近区域

part = video_html[
    pos:
    ]



from urllib.parse import urlparse, parse_qs, unquote


# 先从关键词附近内容提取网址
urls = re.findall(
    r'https?://[^\s"\']+',
    content_part
)


real_urls = []


for u in urls:

    # YouTube redirect解析

    if "youtube.com/redirect" in u:

        parsed = urlparse(u)

        params = parse_qs(parsed.query)

        if "q" in params:

            real = params["q"][0]

            real = unquote(real)

            real_urls.append(real)


    else:

        real_urls.append(u)



print()
print("真实网址:")


for i,u in enumerate(real_urls,1):

    print(i,u)



# 自动跟踪短链接

final_urls=[]


for u in real_urls:

    try:

        r=requests.get(
            u,
            headers=headers,
            allow_redirects=True,
            timeout=15
        )

        print()
        print("跳转:")
        print(r.url)


        final_urls.append(r.url)


    except Exception as e:

        print(e)



with open(
    "links.txt",
    "w",
    encoding="utf-8"
) as f:

    for u in final_urls:
        f.write(u+"\n")
