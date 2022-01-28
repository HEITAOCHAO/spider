import requests

url = "http://192.168.1.120:3000/user/login"
data = {
    "user_name": "guochao",
    "password": "Gc@123"
}
session = requests.session()

# 登录后，使用session请求，cookie信息在session
resp = session.post(url, data=data)
header = {
    "Cookie": "i_like_gitea=f2d52aad8320e852; lang=zh-CN; _csrf=JEPlPrdLRZB_xrIQ_0naSJ2B3dY6MTY0MjE0NTM4OTAxNzE0MzY4Nw"
}
resp = session.get("http://192.168.1.120:3000/hg/newspaper_spider")

# 也可以使用headers方式请求
resp = requests.get("http://192.168.1.120:3000/hg/newspaper_spider", headers=header)
print(resp.text)
