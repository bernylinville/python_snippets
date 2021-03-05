# coing:utf-8

import json
import time
import multiprocessing

class Work(object):
    def __init__(self, q):
        self.q = q

    def send(self, message):
        if not isinstance(message, str):
            message = json.dumps(message)
        self.q.put(message)

    def recv(self):
        while 1:
            result = self.q.get()
            try:
                res = json.loads(result)
            except:
                res = result
            print('revc is %s' % res)

    def send_all(self):
        for i in range(10):
            self.q.put(i)
            time.sleep(1)

if __name__ == "__main__":
    q = multiprocessing.Queue()
    work = Work(q)
    send = multiprocessing.Process(target=work.send, args=({'name': 'kyle'},))
    recv = multiprocessing.Process(target=work.recv)
    send_all_P = multiprocessing.Process(target=work.send_all)

    send_all_P.start()
    send.start()
    recv.start()

    send_all_P.join()
    recv.terminate()
