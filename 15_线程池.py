from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from threading import Thread


class MyThread(Thread):
    def __init__(self, task):
        super(self.__class__, self).__init__()
        self.task = task

    def run(self):
        for i in range(1000):
            print(f"任务ID={self.task},num={i}")


if __name__ == '__main__':
    # 创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            myThread = MyThread(i)
            myThread.start()
            t.submit(myThread)
