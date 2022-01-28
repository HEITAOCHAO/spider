import requests
import asyncio
import aiohttp
import aiofiles
from lxml import etree

requests.packages.urllib3.disable_warnings()
book_url = "https://www.xbiquge.la/11/11433/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}
resp = requests.get(book_url, headers=header, verify=False)
resp.encoding = "utf-8"
# print(resp.text)
html = etree.HTML(resp.text)
dl = html.xpath('//*[@id="list"]/dl')[0]


async def download(name, url):
    print(book_url + url)
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False), headers=header) as session:
        async with session.get(book_url + url) as child_resp:
            resp.encoding = "utf-8"
            text = await child_resp.text()
            child_html = etree.HTML(text)
            content = "".join(child_html.xpath('//*[@id="content"]/text()'))
            async with aiofiles.open(f"./novel/{name}.txt", "w", encoding="utf-8") as f:
                await f.write(content)


async def main():
    task = []
    for catalog in dl.xpath("./dd"):
        href = catalog.xpath("./a/@href")[0].split("/")[-1]
        title = catalog.xpath("./a/text()")[0]
        task.append(asyncio.create_task(download(title, href)))
    await asyncio.wait(task)


if __name__ == '__main__':
    # asyncio.run(main())

    loop = asyncio.get_event_loop()  # 可以防止报错
    loop.run_until_complete(main())
