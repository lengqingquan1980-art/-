import requests

print("===== Network Test =====")

url = "https://www.google.com"

response = requests.get(url)

print("Status Code:", response.status_code)
print("Server:", response.headers.get("server"))
print("Content Length:", len(response.text))
