# coding:utf-8

import multiprocessing,time,random

def sender(q):
    while True:
        x = random.randint(1, 10)
        print("send done: ", x)
        q.put(x)
        time.sleep(1)

def recvder(q):
    while True:
        x = q.get()
        print("recv done: ", x * 3.14)
        time.sleep(1)

if __name__ == "__main__":
    q = multiprocessing.Queue()
    t1 = multiprocessing.Process(target=sender, args=(q,))
    t2 = multiprocessing.Process(target=recvder, args=(q,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
