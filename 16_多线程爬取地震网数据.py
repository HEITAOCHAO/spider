import requests
import json
import csv
from requests.adapters import HTTPAdapter
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

requests.packages.urllib3.disable_warnings()

f = open("./csv/地震.csv", "w", newline="")
csvwrite = csv.writer(f)

# 重试
session = requests.Session()
session.mount('http://', HTTPAdapter(max_retries=3))
session.mount('https://', HTTPAdapter(max_retries=3))


def get_data(page):
    # 数据api
    url = f"https://www.ceic.ac.cn/ajax/search?page={page}&&start=1990-01-01&end=2022-01-16&jingdu1=&jingdu2=&weidu1=&weidu2=&height1=&height2=&zhenji1=&zhenji2="
    try:
        resp = session.get(url, verify=False, timeout=5)
        data = json.loads(resp.text.replace("(", "").replace(")", ""))["shuju"]
        for i in range(len(data)):
            lat = data[i]["EPI_LAT"]
            lon = data[i]["EPI_LON"]
            location = data[i]["LOCATION_C"]
            level = data[i]["M"]
            date = data[i]["O_TIME"]
            depth = data[i]["EPI_DEPTH"]
            csvwrite.writerow([lat, lon, location, level, date, depth])
        print(url, "over!")
    except BaseException:
        print(url, "error!")


if __name__ == '__main__':
    t1 = time.time()
    with ThreadPoolExecutor(5) as t:
        for i in range(1, 480):
            t.submit(get_data, i)
    print(time.time() - t1)

f.close()
