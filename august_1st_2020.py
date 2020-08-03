'''
17 python代码得到2个列表的交集与差集 不许用set
交集思路：遍历list1，判断是否在list2中，在的话，则存入一个列表中。
差集思路：分别遍历list1和2，如果不在对方的list中，则存入一个列表中
'''

# def jiaoji_chaji(ali,bli):
#     jiaoji = []
#     chaji = []
#     for i in range(len(ali)):
#         if ali[i] in bli:
#             jiaoji.append(ali[i])
#     for x in range(len(ali)):
#         if ali[x] not in bli:
#             chaji.append(ali[x])
#     for y in range(len(bli)):
#         if bli[y] not in ali:
#             chaji.append(bli[y])
#     print('交集是',jiaoji)
#     print('差集是',chaji)
#
# jiaoji_chaji([1,3,5,6,7],[1,2,4,6,7]) #交集[1,6,7] #差集[3,5,2,4]

'''
18 写一个函数，这个函数要计算浮点数乘法的一万次相乘后的时间耗时，浮点数可以使用随机小数
'''

# import time,random
# def jisuan_shihao():
#     start = time.time()
#     for i in range(1,10001):
#         random.uniform(1,3) * random.uniform(1,3)
#     stop = time.time()
#     print(stop-start)
# jisuan_shihao()

'''
19 定义函数add(a,b)要求有个值是result来存结果

1 a,b 数字，相加
2 a,b 字符串，就当做字符串相加
3 a,b 如果list就当list相加
'''

# def print_add(a,b):
#     result = a+b
#     print(result)
# print_add([1,2],[2,4])

'''
20 函数参数传入5个字母，声明一个可变参数的函数，拼成一个单词
'''

# def print_kebiancanshu(*w):
#     st = ''
#     for i in w:
#         st += i
#     print(st)
# print_kebiancanshu('a','p','p','l','e')


'''
21 使用必填参数、默认参数、可变元组参数、可变字典参数（value）计算一下单词的长度之和
'''

# def print_dancichangdu(a,b='ss',*agr,**key):
#     result = ''
#     result += a
#     result += b
#     for i in agr:
#         result += i
#     for v in key.values():
#         result += v
#     print(result,'长度为',len(result))
# print_dancichangdu('red','sss','blue','purple',**{'ab': 'cd'})

'''
22 使用map把[1,2,3]变为[2,3,4]
'''

# def print_gaibianzhi(l):
#     return l+1
# obj = map(print_gaibianzhi,[4,5,6])
# print(list(obj))

'''
23 使用map，大写变小写
'''

# def print_dabianxiao(s):
#     return s.lower()
# abj = map(print_dabianxiao,['A'])
# print(list(abj))

'''
24 打印2000-3000之间被7整除但不被5整除的数，以，(逗号)分隔
'''

# def print_zhengchu():
#     a = []
#     for i in range(2000,3001):
#         ab = True
#         if i %7 == 0 and i %5 != 0:
#             print(i,end=',')
# print_zhengchu()






