'''
25 计算1 - 1/2 + 1/3 - 1/4 + … + 1/99 - 1/100 + …直到最后一项的绝对值小于10的-5次幂为止
'''

# import math
# def print_Calculation():
#     sum = 1
#     a = 1
#     while True:
#         a += 1
#         if abs(1/a) < pow(10,-5):
#             break
#         elif a %2 == 0:
#             sum -= 1/a
#         else:
#             sum += 1/a
#     print(sum)
# print_Calculation()


# def print_fivemi():
#     result = 0.0
#     n = 1
#     while True:
#         if abs(1/n) < pow(10,-5):
#             break
#         else:
#             if n%2 ==1:
#                 result += 1/n
#                 n += 1
#             else:
#                 result -= 1/n
#                 n += 1
#     print(result)
# print_fivemi()

'''
26 编程将类似“China”这样的明文译成密文，
密码规律是：用字母表中原来
的字母后面第4个字母代替原来的字母，不能改变其大小写，如果超出了字母
表最后一个字母则回退到字母表中第一个字母

'''

# import sys
# def print_mingwen_miwen(s):
#     result = ''
#     if not isinstance(s,str):
#         sys.exit(1)             #正常结束~
#     for i in s:
#         if (i >= 'a' and i<='v') or (i >= 'A' and i<='V'):
#             result += chr(ord(i)+4)
#         else:
#             result += chr(ord(i)-22)
#     return result
# print(print_mingwen_miwen('china'))

'''
27 输出以下如下规律的矩阵
1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20

思路：先用一条for语句控制行数，再用一条for控制列数，规律是行和列相乘
'''

# def print_juzhenguilv():
#
#     for i in range(1,5):
#         for j in range(1,6):
#             print(i*j,end=' ')
#         print()
#
# print_juzhenguilv()

'''
28 对一个列表求和，如列表是[4, 3, 6]，求和结果是 [4, 7, 13]，每一项的值都等与该项的值加上前一项的值
'''

# def liebiao_qiuhe(n):
#     li = []
#     sum = 0
#     for i in range(len(n)):
#         sum += n[i]
#         li.append(sum)
#     return li
# print(liebiao_qiuhe([4,3,6]))


'''
29 一个字符串 list，每个元素是 1 个 ip，输出出现次数最多的 ip
'''

# def print_listip(list):
#     for i in list:
#
#         print(id(i))
#
# print_listip([1,2,3,3])


# def print_ip():
#     num_list = ["168.1.1.1","168.1.1.1","168.1.1.2","168.1.1.3"]
#     num_dict = {}
#     for i in num_list:
#         if i not in num_dict.keys():
#             num_dict[i] = 1
#         else:
#             num_dict[i] += 1
#         #一句可以搞定
#         #num_dict[i] = num_list.count(i)
#     for k,v in num_dict.items():
#         if v == max(num_dict.values()):
#             print("出现次数最多的IP：",k)
#
# print_ip()

'''
30 实现一个简易版的计算器，功能要求：加、减、乘、除，支持多数同时进行计算

'''

# def jianyi_jisuanqi():
#
#
#
# jianyi_jisuanqi()



