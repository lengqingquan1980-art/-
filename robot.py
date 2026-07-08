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
    pos + 3000
]



print()
print("正在解析真实网址...")



# 方法1:
# 找 urlEndpoint 里的真实链接

urls = re.findall(
    r'"urlEndpoint":\{"url":"(.*?)"',
    part
)



# 方法2:
# 找普通https

if not urls:

    urls = re.findall(
        r'https?://[^"\\ ]+',
        part
    )



result=[]


for u in urls:

    u = u.replace(
        "\\u0026",
        "&"
    )

    u = u.replace(
        "\\/",
        "/"
    )

    if u not in result:

        result.append(u)



print()
print("找到网址数量:")
print(len(result))



for i,u in enumerate(result,1):

    print()
    print(i,u)



# 保存

with open(
    "links.txt",
    "w",
    encoding="utf-8"
) as f:

    for u in result:
        f.write(u+"\n")



print()
print("完成，已保存 links.txt")
