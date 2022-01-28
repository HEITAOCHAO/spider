import requests

url = "http://122.51.248.121:8910/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}
proxies = {
    "http": "http://47.113.180.76:81"
}
# while True:
resp = requests.get(url, proxies=proxies)
resp.encoding = "utf-8"
print(resp.text)
