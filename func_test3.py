# import time
# def i_can_sleep():
#     time.sleep(2)
#
# start = time.time()
# i_can_sleep()
# stop = time.time()
# print(start,stop)

import datetime
# def fun1():
#     start = fun1.datetime()
#     print(start)
# fun1()



# a * x + b = y

# def a_line(a,b):
#     def addy(x):
#         return a * x + b
#     return addy
#
# line1 = a_line(2,3)
# print(line1(10))

# 求1+2!+3!+...+20!的和
def fun2(b):
    a = 1
    for i in range(1,b+1):
        a = a * i
    return a
# print(fun2(5))

def fun1(a):
    b = 0
    for i in range(1,a+1):
        b = b + fun2(i)
    return b

print(fun1(3))
print(fun1(5))
print(fun1(10))
# print(fun1(20))

