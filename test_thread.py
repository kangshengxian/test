import threading
import time
from threading import  current_thread      #引用获取线程名称函数

def myThread(arg1, arg2):
    print(current_thread().getName(),'start')      #获取线程名称
    print('%s %s' %(arg1, arg2))
    time.sleep(1)
    print(current_thread().getName(),'stop')
for i in range(1,6,1):
    t1 = threading.Thread(target=myThread,args=(i, i+1))    #创建线程
    t1.start()      #开启线程

print(current_thread().getName(),'end')
