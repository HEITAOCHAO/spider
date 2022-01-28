import requests

url = "https://www.pearvideo.com/video_1644002"
# 获取contId
contId = url.split("_")[1]
# 进行封装
api = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.742299109613463"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    # 防盗链
    "Referer": url
}
# 加上header进行获取接口数据
resp = requests.get(api, headers=header)
dic = resp.json()
# 获取视频链接
src = dic["videoInfo"]["videos"]["srcUrl"]
# 获取系统时间
systemTime = dic["systemTime"]
# 把原视频地址修改成可直接访问
videoUrl = src.replace(systemTime, f"cont-{contId}")
# 进行下载
with open("./video/梨视频.mp4", "wb") as f:
    f.write(requests.get(videoUrl).content)


