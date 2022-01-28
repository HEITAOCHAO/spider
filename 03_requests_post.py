import requests

url = "https://fanyi.baidu.com/sug"
work = input("请输入单词")
data = {
    "kw": work
}
resp = requests.post(url, data=data)

print(resp)
print(resp.json())
resp.close()