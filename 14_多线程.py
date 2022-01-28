from threading import Thread


def fun1(name):
    for i in range(1000):
        print(f"{name}:{i}")


class MyThread(Thread):
    def __init__(self, name):
        super(self.__class__, self).__init__()
        self.name = name

    def run(self):
        for i in range(1000):
            print(f"{self.name}:{i}")


if __name__ == '__main__':
    # 注意 target=fun1() 这种是调用的方法的返回值，要等待方法的返回之后才能进行下一步 所以多线程就不起作用
    # target=fun1才是调用方法本身，如果传参使用 args= 元组 最后必须跟个逗号，
    t1 = Thread(target=fun1, args=("帅哥",))
    t1.start()
    # 定义的类放在 main方法上 才能解析
    myTread = MyThread("刘亦菲")
    myTread.start()
    for i in range(1000):
        print(f"美女:{i}")
