import requests
import re

url = "https://www.youtube.com/@berrypassnet/videos"

headers = {
    "User-Agent": "Mozilla/5.0"
}

html = requests.get(url, headers=headers).text

video_ids = re.findall(r'"videoId":"([a-zA-Z0-9_-]{11})"', html)

# 去重，并保持原顺序
unique = []

for vid in video_ids:
    if vid not in unique:
        unique.append(vid)

print("共找到", len(unique), "个视频")

print()

for i, vid in enumerate(unique, 1):
    print(f"{i}. https://www.youtube.com/watch?v={vid}")
