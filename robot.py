import requests
import re

url = "https://www.youtube.com/@berrypassnet/videos"

headers = {
    "User-Agent": "Mozilla/5.0"
}

html = requests.get(url, headers=headers).text

print("网页长度：", len(html))

print("\n开始寻找视频ID...\n")

video_ids = re.findall(r'"videoId":"([a-zA-Z0-9_-]{11})"', html)

print("找到数量：", len(video_ids))

print()

for vid in video_ids[:20]:
    print(vid)
