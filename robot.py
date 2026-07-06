import requests

url = "https://www.youtube.com/@berrypassnet/videos"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print("Status:", response.status_code)
print("Length:", len(response.text))

print()
print("===== First 1000 characters =====")
print(response.text[:1000])
