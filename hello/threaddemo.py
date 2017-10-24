#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import threading

def ask():
    for i in range(100):
        print ('ask'+str(i))



def ans():
    for i in range(100):
        print ('ans'+str(i))


def test():
    threads = []
    t1=threading.Thread(target=ask)
    t2=threading.Thread(target=ans)
    t3=threading.Thread(target=ans)
    threads.append(t1)
    threads.append(t2)
    threads.append(t3)
    for t in threads:
        t.start()


if __name__ == '__main__':
    test()


## 父子线程
import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

# 锁

balance = 0
lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            #change_it(n)
            print 1
        finally:
            # 改完了一定要释放锁:
            lock.release()