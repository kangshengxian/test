# 创建一个函数，用于接收用户输入的数字，并计算用户输入数字的和

# def num():
#     n1 = int(input('请输入第一个整数:'))
#     n2 = int(input('请输入第二个整数:'))
#     print('这两个数字的和是:%s + %s = %s' %(n1,n2,n1+n2))
# num()

# def num2():
#     n_num = input('请输入多个整数（中间用空格隔开，回车确认）：')
#     n_list = n_num.split(' ')
#     s = 0
#     for i in range(len(n_list)):
#         s += int(n_list[i])
#     print('这些数的和是：%s' % (s))
# num2()

# 创建一个函数，传入n个整数，返回其中最大的数和最小的数

# def fun(*nums):
#     print('最大的数是：%s' %max(nums))
#     print('最小的数是：%s' %min(nums))
# fun(1,2,3,5,6,8,9)
#
# # 创建一个函数，传入一个参数n，返回n的阶乘
#
# def fun1(n):
#
#     a = 1
#     for x in range(1,n+1):
#         a = a * x
#     # print(a)
#     return a
# print('5的阶乘是：%s' %fun1(5))

# def hl(first, *other):
#     print(1 + len(other))
# hl(111,222,333)



