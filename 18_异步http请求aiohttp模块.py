import aiohttp
import asyncio

urls = [
    "https:///uploadfile/pic/20211003/1975_0_ECKFxtDcA6qstQkMyjSk.jpg",
    "https:///uploadfile/pic/20211003/1975_1_J3RWhWlaM4Ja5c1rhSLs.jpg",
    "https:///uploadfile/pic/20211003/1975_2_8P4fpL4vBreRvNT3cQx4.jpg",
    "https:///uploadfile/pic/20211003/1975_3_bA0NfsM2qPFcfzSd2itL.jpg",
    "https:///uploadfile/pic/20211003/1975_4_UrWeYBDSpremtBPAI8os.jpg",
    "https:///uploadfile/pic/20211003/1975_5_Uds0h9SBPl4k4BS5a6d5.jpg",
    "https:///uploadfile/pic/20211003/1975_6_9mckraIXbeqIpsoqYlP3.jpg",
    "https:///uploadfile/pic/20211003/1975_7_vOEaMAn0jkWQiW3wcyUe.jpg",
    "https:///uploadfile/pic/20211003/1975_9_QAOnCEYvuk1Ly3BzE0Kw.jpg"
    "https:///uploadfile/pic/20211003/1975_8_eqt5ZQyoR7QlYYd7jCW9.jpg",
]

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
   
}


async def download_img(url):
    name = url.rsplit("/", 1)[1]  # 从右边分割,分割一次,取下标为1的
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:  # 相当于requests
        async with session.get(url) as resp:  # 相当于 requests.get()
            # 请求回来,写入文件
            with open(name, "wb") as f:
                f.write(await resp.content.read())

    # aiohttp中的 resp.text()   <==>  requests 的 resp.text
    # aiohttp中的 resp.content().read()   <==>  requests 的 resp.content


async def main():
    task = []
    for url in urls:
        fun = download_img(url)
        task.append(asyncio.create_task(fun))
    await asyncio.wait(task)


if __name__ == '__main__':

    # asyncio.run(main())

    loop = asyncio.get_event_loop()  # 可以防止报错
    loop.run_until_complete(main())



