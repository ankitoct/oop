from threading import *
from time import sleep


class Hello(Thread):
    def run(self):
        for i in range(10):
            print("Hello")
            sleep(1)
class Hiii(Thread):
    def run(self):
        for i in range(10):
            print("HIII")
            sleep(1)
t1=h=Hello()
t2=Hiii()
t1.start()
print(t1.getName())
t2.start()
t2.setName("thread2")
print(t2.getName())
