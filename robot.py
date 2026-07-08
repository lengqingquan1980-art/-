import requests
import re


# ==========================
# 目标频道
# ==========================

channel_url = "https://www.youtube.com/@SFZY666/videos"


headers = {
    "User-Agent": "Mozilla/5.0"
}


# ==========================
# 获取频道页面
# ==========================

print("正在获取频道页面...")

html = requests.get(
    channel_url,
    headers=headers
).text


# ==========================
# 提取视频ID
# ==========================

video_ids = re.findall(
    r'"videoId":"([a-zA-Z0-9_-]{11})"',
    html
)


# 去重

unique = []

for vid in video_ids:
    if vid not in unique:
        unique.append(vid)


print()
print("找到视频数量:", len(unique))


if len(unique) == 0:
    print("没有找到视频")
    exit()


# 最新视频

latest_video = unique[0]


print()
print("最新视频ID:")
print(latest_video)


video_url = (
    "https://www.youtube.com/watch?v="
    + latest_video
)


print()
print("视频地址:")
print(video_url)



# ==========================
# 获取视频页面
# ==========================

print()
print("正在读取视频介绍...")


video_html = requests.get(
    video_url,
    headers=headers
).text


print()
print("页面长度:")
print(len(video_html))



# ==========================
# 查找关键词
# ==========================

keyword = "最新免费节点获取地址"


print()


if keyword not in video_html:

    print("没有找到关键词")
    exit()



print("找到关键词！")



# ==========================
# 提取关键词附近内容
# ==========================

index = video_html.find(keyword)


text = video_html[index:index + 5000]



# ==========================
# 提取URL
# ==========================

print()
print("开始寻找网址...")


urls = re.findall(
    r'https?://[^"\\\s<>]+',
    text
)



# 去重

url_list = []

for url in urls:

    if url not in url_list:
        url_list.append(url)



print()


if len(url_list) == 0:

    print("没有找到网址")


else:

    print("找到网址数量:", len(url_list))


    for i, url in enumerate(url_list, 1):

        print()
        print(i, url)
