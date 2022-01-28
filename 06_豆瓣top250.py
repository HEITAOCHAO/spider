import re
import requests
import csv

url = "https://movie.douban.com/top250"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}
resp = requests.get(url, headers=header)
html = resp.text
resp.close()

obj = re.compile('div class="item">.*?<span class="title">'
                 '(?P<name>.*?)</span>.*?<p class="">.*?<br>'
                 '(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">'
                 '(?P<score>.*?)</span>.*?</span>.*?<span>'
                 '(?P<num>.*?)人评价</span>', re.S)

f = open("./csv/豆瓣top电影.csv", "w")
csvWriter = csv.writer(f)

item = obj.finditer(html)
for it in item:
    # print(f"name={it.group('name')},year={it.group('year')},score={it.group('score')},num={it.group('num')}")
    dic = it.groupdict()
    print(type(it.groupdict()))
    dic["year"] = dic["year"].strip()
    csvWriter.writerow(dic.values())

f.close()
