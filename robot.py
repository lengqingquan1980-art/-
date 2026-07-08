import requests
import re


# 目标频道
channel_url = "https://www.youtube.com/@SFZY666/videos"


headers = {
    "User-Agent": "Mozilla/5.0"
}


# ==========================
# 1. 获取频道页面
# ==========================

html = requests.get(channel_url, headers=headers).text


# ==========================
# 2. 提取视频ID
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


print("找到视频数量:", len(unique))


if len(unique) == 0:
    print("没有找到视频")
    exit()


# 最新视频
latest_video = unique[0]


print()
print("最新视频ID:")
print(latest_video)


video_url = f"https://www.youtube.com/watch?v={latest_video}"

print()
print("视频地址:")
print(video_url)


# ==========================
# 3. 获取视频页面
# ==========================

video_html = requests.get(
    video_url,
    headers=headers
).text


print()
print("视频页面长度:")
print(len(video_html))


# ==========================
# 4. 查找节点地址关键词
# ==========================

keyword = "最新免费节点获取地址"


print()

if keyword in video_html:

    print("找到关键词！")


    # 截取关键词附近内容
    index = video_html.find(keyword)

    around = video_html[index:index+1000]

    print()
    print("附近内容:")
    print(around)


else:

    print("没有找到关键词")
