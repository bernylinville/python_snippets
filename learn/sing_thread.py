# coding:utf-8

import threading

def sing():
    for i in range(3):
        print("singing...")

if __name__ == "__main__":
    sing_thread = threading.Thread(target=sing, name="sing_thread")
    sing_thread.start()
