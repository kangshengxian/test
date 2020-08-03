


# a = [3,4,5,6,7]
#
# b = []
# for i in a:
#    b.append(i*2)
# print(b)
#
# b = [i*2 for i in a]
# print(b)
# [6,8,10,12,14]

# for x in range(1,10):
#     line = ''
#     for y in range(1,x+1):
#         a = "%d*%d=%d" % (x,y,x*y)
#         line = line +" "+ a
#
#     print(line)




# 有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？

# a = []
# b = 0
# for x in range(1,5):
#     for y in range(1,5):
#         for z in range(1,5):
#             if x!=y and y!=z and z!=x:
#                 res = x*100+y*10+z
#                 a.append(res)
#                 b += 1
# print(a,b)


# n = 100
#
# sum = 0
# counter = 1
# while counter <= n:
#     sum = sum + counter
#     counter += 1
#
# print("1 到 %d 之和为: %d" % (n, sum))

# var = 1
# while var == 1:  # 表达式永远为 true
#     num = int(input("输入一个数字  :"))
#     print("你输入的数字是: ", num)
# print("Good bye!")



# b = 1
# sum = 0
# while b <= 100:
#
#     sum += b
#     b += 1
# print('0-100之间的和为：%s' %sum)



# count = 0
# while count < 5:
#    print (count, " 小于 5")
#    count = count + 1
# else:
#    print (count, " 大于或等于 5")

# sites = ["Baidu", "Google","Runoob","Taobao"]
# for site in sites:
#     if site == "Runoob":
#         print("菜鸟教程!")
#         break
#     print("循环数据 " + site)
# else:
#     print("没有循环数据!")
# print("完成循环!")


# a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
# for i in range(len(a)):
#     print(i,a[i])
#
#
# print(list(range(11)))


# for n in range(101, 200):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, '等于', x, '*', n//x)
#             break
#     else:
#         # 循环中没有找到元素
#         print(n, ' 是质数')


# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
# for x in it:
#     print (x, end=" ")


# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
#
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
#
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# for x in myiter:
#     print(x)


# for char in 'PYTHON STRING':
#     if char == ' ':
#         break
#
#     print(char, end='')
#
#     if char == 'O':
#         continue


# import random
# tmp=''
# for i in range(4):
#     n=random.randrange(0,2)
#     if n==0:
#         num = random.randrange(65, 91)
#         tmp+=chr(num)
#     else:
#         k=random.randrange(0,10)
#         tmp+=str(k)
# print(tmp)

# 实现用户输入用户名和密码，当用户名为 seven且密码为123时，显示登陆成功，否则登陆失败
# 实现用户输入用户名和密码，当用户名为 seven且密码为123时，显示登陆成功，否则登陆失败，失败时允许重复输入三次
# n = 0
# while True:
#     name = input('请输入用户名：')
#     password = input('请输入密码：')
#     if name == 'seven' and password == '123':
#         print('登录成功！~')
#     else:
#         print('登录失败！~')
#         n +=1
#         if n == 3:
#             exit()

# 使用while循环实现输出2-3+4-5+6.....+100的和

# sum = 0
# for i in range(0,100):
#     if i %2 == 0:
#         sum = sum - i
#     else:
#         sum += i
# print(sum)

# a = set()
#
# a.update('h,e,l,l,o')
#
# print(a)


import datetime

