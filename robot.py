import requests
import re
import os

url = "https://www.youtube.com/@berrypassnet/videos"

headers = {
    "User-Agent": "Mozilla/5.0"
}

# 获取网页
html = requests.get(url, headers=headers).text

# 提取视频ID
video_ids = re.findall(
    r'"videoId":"([a-zA-Z0-9_-]{11})"',
    html
)

# 去重
unique = []

for vid in video_ids:
    if vid not in unique:
        unique.append(vid)

print("共找到", len(unique), "个视频")

# 最新视频
latest_video = unique[0]
latest_url = f"https://www.youtube.com/watch?v={latest_video}"

print()
print("最新视频:")
print(latest_video)

# 记忆文件
memory_file = "latest_video.txt"

# 检查以前记录
if os.path.exists(memory_file):

    with open(memory_file, "r") as f:
        old_video = f.read().strip()

    print()
    print("历史记录:")
    print(old_video)

    if latest_video == old_video:

        print()
        print("没有新视频")

    else:

        print()
        print("发现新视频！")
        print(latest_url)

else:

    print()
    print("第一次运行，建立记忆")

# 保存最新记录
with open(memory_file, "w") as f:
    f.write(latest_video)
