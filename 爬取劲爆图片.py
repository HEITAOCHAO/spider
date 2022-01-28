import requests
from lxml import etree
import time
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 去除SSL验证的警告报错
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

index_url = "https://www.***.com"
photo_url = "https://www.***.com/photo/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Referer": "https://www.***.com/"
}

for num in range(18):
    resp = requests.get(photo_url + "?page=" + str(num + 1), headers=header, verify=False, timeout=5)
    html = etree.HTML(resp.text)
    lis = html.xpath("/html/body/div[4]/div/div[3]/ul[1]/li")
    for li in lis:
        # 获取子页面的后缀链接
        href = li.xpath("./a/@href")
        suffix = href[0].split("/")[-1]
        # 获取图片有多少张
        title = li.xpath("./a/div/div[1]/text()")
        page = re.findall(r"\d+", title[0])[-1]
        for i in range(int(page)):
            # 睡1秒调用子页面
            time.sleep(1)
            child_url = photo_url + suffix + "?page=" + str(i + 1)
            img_url = ""
            try:
                child_resp = requests.get(child_url, headers=header, verify=False, timeout=5)
                child_html = etree.HTML(child_resp.text)
                # 获取子页面的图片链接
                src = child_html.xpath("/html/body/div[4]/div[1]/div[1]/nav/a/img/@src")[0]
                # 保存图片的名字
                name = src.split("/")[-1]
                img_url = index_url + src
                img_resp = requests.get(img_url, timeout=5)
                with open(f"./imgs/{name}", "wb") as f:
                    f.write(img_resp.content)
                print("over! " + index_url + src)
            except Exception as e:
                print(f"error:child_url={child_url}")
                print(f"error:img_url={img_url}")
                print(e)
