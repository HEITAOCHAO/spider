from lxml import etree
import requests
import csv

url = "https://chengdu.zbj.com/search/f/?kw=saas"
page = requests.get(url)

f = open("./csv/猪八戒.csv", "w")
csvWriter = csv.writer(f)
# 解析
html = etree.HTML(page.text)
divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div")
for div in divs:
    name = div.xpath("./div/div/a/div/p/text()")[1].strip()
    city = div.xpath("./div/div/a/div/div/span/text()")[0]
    price = div.xpath("./div/div/a/div/div/span/text()")[1].strip("¥")
    title = "saas".join(div.xpath("./div/div/a[2]/div[2]/div[2]/p/text()"))
    csvWriter.writerow([name, city, price, title])
f.close()
