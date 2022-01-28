import requests

url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20"

data = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20"
}
header = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}

resp = requests.get(url=url, params=data, headers=header)



print(resp.request.url)

print(resp.json())

resp.close()