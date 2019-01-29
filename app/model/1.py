#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2019/1/26 上午9:35
# @Author   : Vampire
# @Site     :  
# @File     : 1.py
# @Software : PyCharm

import threading
import random
import time

class MyThread(threading.Thread):
    def __init__(self,threadName,event):
        threading.Thread.__init__(self,name=threadName)
        self.threadEvent = event

    def run(self):
        print ("%s is ready" % self.name)
        self.threadEvent.wait()
        print ("%s run!" % self.name)

    def start(self):
        # self.threadEvent.wait()
        print ("%s start!" % self.name)

sinal = threading.Event()
for i in range(10):
    t = MyThread(str(i),sinal)
    t.start()
print('-----------')
sinal.set()