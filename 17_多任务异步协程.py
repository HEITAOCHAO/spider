import asyncio
import time


async def func1():
    print("你好啊，我叫王宝强！")
    # time.sleep(2)  # 当程序出现同步操作的时候，异步久中断了
    await asyncio.sleep(2)  # 异步操作的代码
    print("你好啊，我叫王宝强！")


async def func2():
    print("你好啊，我叫周杰伦！")
    # time.sleep(3)  # 当程序出现同步操作的时候，异步久中断了
    await asyncio.sleep(3)  # 异步操作的代码
    print("你好啊，我叫周杰伦！")


async def func3():
    print("你好啊，我叫成才！")
    # time.sleep(4)  # 当程序出现同步操作的时候，异步久中断了
    await asyncio.sleep(4)  # 异步操作的代码
    print("你好啊，我叫成才！")


# 一般不这样写法
# if __name__ == '__main__':
#     start = time.time()
#     fun1 = func1()  # 此时的函数是异步协程函数，此时函数执行得到的是一个协程对象
#     fun2 = func2()  # 此时的函数是异步协程函数，此时函数执行得到的是一个协程对象
#     fun3 = func3()  # 此时的函数是异步协程函数，此时函数执行得到的是一个协程对象
#     task = [
#          fun1, fun2, fun3
#     ]
#     # asyncio.run(fun1)  # 协程程序运行需要asyncio模块的支持
#     asyncio.run(asyncio.wait(task))  # 一次性启动多个协程任务
#
#     print(time.time() - start)

# 推荐写法
# async def main():
#     task = [
#         asyncio.create_task(func1()), asyncio.create_task(func2()), asyncio.create_task(func3())
#     ]
#     await asyncio.wait(task)
#
#
# if __name__ == '__main__':
#     start = time.time()
#     asyncio.run(main())
#     print(time.time() - start)


#   模拟爬虫
async def download(url):
    print("准备开始下载")
    await asyncio.sleep(2)  # 当作网络请求
    print("下载完成")


async def main():
    urls = [
        "http://www.baidu.com",
        "http://www.sougou.com",
        "http://www.souhu.com",
    ]

    # task = []
    # for url in urls:
    #     func = download(url)
    #     task.append(asyncio.create_task(func))

    tasks = [asyncio.create_task(download(url)) for url in urls]  # for循环也可以这么写
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
