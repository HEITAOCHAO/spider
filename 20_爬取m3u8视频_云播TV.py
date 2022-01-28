import time

import requests
import re
import aiohttp
import aiofiles
import asyncio
# pip install pycryptodome
from Crypto.Cipher import AES
import os
import math

# 清除SSL报错
requests.packages.urllib3.disable_warnings()
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}

ts_num = 0


# 获取第一次m3u8地址
def get_first_m3u8_url(url):
    resp = requests.get(url, verify=False, headers=header)
    obj = re.compile(r'"url":"(?P<url>.*?)"', re.S)
    urls = re.finditer(obj, resp.text)
    first_m3u8_url = ""
    for it in urls:
        if "m3u8" in it.group():
            first_m3u8_url = it.group("url")
    return first_m3u8_url


# 读取第二次m3u8地址并下载
def read_second_m3u8_url_download(url):
    with open("./m3u8/first_m3u8.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("#"):
                continue
            else:
                download(url + line, "second_m3u8.txt")


# 下载m3u8文件
def download(url, name):
    print(url)
    resp = requests.get(url, verify=False, headers=header)
    with open(f"./m3u8/{name}", "wb") as f:
        f.write(resp.content)


# 异步协程下载文件 2
async def download_ts(url, session):
    ts_name = url.split("/")[-1]
    try:
        async with session.get(url) as resp:
            async with aiofiles.open(f"./ts/{ts_name}", "wb") as f:
                await f.write(await resp.content.read())
            print(ts_name, "下载完毕！")
    except BaseException as e:
        print(f"error,url={url},msg={e}")
        await asyncio.wait(asyncio.create_task(download_ts(url, session)))


# 异步协程下载文件(封装协程对象)
async def aio_download():
    task = []
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open("./m3u8/second_m3u8.txt", "r", encoding="utf-8") as f:
            async for line in f:
                line = line.strip()
                if line.startswith("#"):
                    continue
                fun = download_ts(line, session)
                task.append(asyncio.create_task(fun))
            await asyncio.wait(task)


# 获取加密信息字符串
def get_key():
    url = ""
    with open("./m3u8/second_m3u8.txt", "r", encoding="utf-8") as f:
        for line in f:
            if "EXT-X-KEY" in line:
                line = line.strip()
                url = re.search(r'URI="(?P<url>.*?)"', line).group("url")
                break
    return requests.get(url).text


# 解码ts
async def decrypt_ts(name, key):
    # IV偏移量，字节和key的长度一样16个0
    aes = AES.new(key=bytes(key, encoding='utf8'), mode=AES.MODE_CBC, iv=b'0000000000000000')
    async with aiofiles.open(f"./ts/{name}", "rb") as fr, \
            aiofiles.open(f"./temp/{name}", "wb") as fw:
        bs = await fr.read()
        await fw.write(aes.decrypt(bs))


# 创建解码协程对象任务
async def aio_decrypt(key):
    task = []
    async with aiofiles.open("./m3u8/second_m3u8.txt", "r", encoding="utf-8") as f:
        async for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            name = line.split("/")[-1]
            task.append(asyncio.create_task(decrypt_ts(name, key)))
        await asyncio.wait(task)


# 视频合并
def merge(name):
    """
    windows     copy /b 1.ts+2.ts+3.ts av.mp4
    linux       cat 1.ts 2.ts 3.ts > av.mp4
    :return:
    """
    lst = []
    with open("./m3u8/second_m3u8.txt", "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            line = line.split("/")[-1]
            lst.append(line)
    new_lst = []
    # 切换路径
    os.chdir("temp")
    if len(lst) < 101:
        str = "+".join(lst)
        os.system(f"copy /b {str} {name}")
    else:
        num = math.ceil(len(lst) / 100)
        for i in range(num):
            if i != (num - 1):
                new_lst.append("+".join(lst[i * 100:(i + 1) * 100]))
            else:
                new_lst.append("+".join(lst[i * 100:]))

    new_ts = []
    for i in range(len(new_lst)):
        new_ts.append(f"{i}.ts")
        os.system(f"copy /b {new_lst[i]} {i}.ts")

    str2 = "+".join(new_ts)
    os.system(f"copy /b {str2} {name}")

    # 删除 temp中的文件
    for f in lst:
        try:
            os.remove(f"{f}")
        except BaseException as e:
            print(f"remove {f} error:{e}")

    # 删除 ts中的文件
    os.chdir("../ts")
    for f in lst:
        try:
            os.remove(f"{f}")
        except BaseException as e:
            print(f"remove {f} error:{e}")


def main(url, name):
    # 获取第一次m3u8地址
    first_m3u8_url = get_first_m3u8_url(url)
    first_m3u8_url = first_m3u8_url.replace("\\", "")
    index_url = first_m3u8_url.split(".com/")[0] + ".com"
    # 下载到本地
    download(first_m3u8_url, "first_m3u8.txt")
    read_second_m3u8_url_download(index_url)
    # 异步协程下载ts文件
    loop = asyncio.get_event_loop()  # 可以防止报错
    loop.run_until_complete(aio_download())
    # 异步协程解析原ts文件
    asyncio.run(aio_decrypt(get_key()))
    # 合并视频
    merge(name)


if __name__ == '__main__':
    start = time.time()
    # url = "https://www.yunbtv.net/vodplay/doupocangqiongtebiepian3-1-13.html"
    url = "https://www.yunbtv.net/vodplay/kaiduan-1-10.html"
    main(url, "开端10.mp4")

    print(f"共耗时：{time.time() - start}")
