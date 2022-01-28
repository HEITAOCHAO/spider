import requests

name = input("请输入明星名字")
url = f'https://www.sogou.com/web?query={name}'

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}

resp = requests.get(url, headers=header)

print(resp)
print(resp.text)
resp.close()