import requests
import time
from bs4 import BeautifulSoup

url = "http://www.netbian.com/weimei/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}

for i in range(50):
    newUrl = url
    if i != 0:
        newUrl = newUrl + "index_" + str(i) + ".html"
    resp = requests.get(newUrl)
    resp.encoding = "gbk"

    page = BeautifulSoup(resp.text, "html.parser")
    div = page.find("div", class_="list")
    # todo  这儿有点毛病，第二页好像没获取到
    images = div.find_all("img")
    for img in images:
        # bs4可以通过get获取属性
        src = img.get("src")
        child_resp = requests.get(src)
        # -1取最后一个
        name = src.split("/")[-1]
        # with open 是自愈的，相当于套了已成 try catch
        with open("img/" + name, "wb") as f:
            f.write(child_resp.content)
        time.sleep(2)
