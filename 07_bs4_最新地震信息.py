import requests
from bs4 import BeautifulSoup
import csv

url = "https://news.ceic.ac.cn/index.html"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}
# verify=False去掉安全验证
resp = requests.get(url, headers=header, verify=False)
# 指定字符集
resp.encoding = "utf-8"
# 指定html解析器
page = BeautifulSoup(resp.text, "html.parser")
# class是关键字
# table = page.find_all("table", class_="news-table")
# 和上面一样
table = page.find("table", attrs={"class": "news-table"})

f = open("./csv/地震.csv", "w")
csvWriter = csv.writer(f)
trs = table.find_all("tr")
for it in trs:
    tds = it.find_all("td")
    arr = []
    for td in tds:
        arr.append(td.text)
    if len(arr) != 0:
        csvWriter.writerow(arr)
f.close()
