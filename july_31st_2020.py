'''
1 写一个函数实现一个数学公式
a**b
'''

# def math_cif(a,b):
#     c = 1
#     for i in range(1,b+1):
#         c *= a
#     print(c)
# math_cif(2,2)

'''
2 求100个随机数之和，随机数求为0—9的整数
'''

# def num_random():
#     from random import randint
#     li = []
#     sum = 0
#     for i in range(1,101):
#         num = randint(0,9)
#         li.append(num)
#         sum += num
#     print(li)
#     print('这些随机数的和为：',sum)
# num_random()

'''
3 要求在屏幕上分别显求1到100之间奇数之和与偶数之和
'''

# def jiou_sum():
#     jsum = 0
#     osum = 0
#     for i in range(1,101):
#         if i %2 == 1:
#             jsum += i
#         else:
#             osum += i
#     print('1-100 奇数和为',jsum,'偶数和为',osum)
# jiou_sum()

'''
4 输入10个数，并显示最大的数与最小的数
'''

# def max_min():
#     li = []
#     for i in range(1,6):
#         num = int(input('请输入第 %s 个数' %i))
#         li.append(num)
#     print(max(li),min(li))
# max_min()

'''
5 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出 各位数字
'''

# def num_nix():
#     while True:
#         num = input('请输入一个不多于五位的正整数：')
#         if len(num) > 5:
#             print('你输入的数超过了五位，请重输！')
#             continue
#
#         print('它是 %s 位数' %len(num),'逆序结果为',num[::-1])
#         break
# num_nix()

'''
6 求1000以内的所有水仙花数（水仙花数：它的每个位上的数字的 n 次幂 之和等于它本身，例如：1^3 + 5^3+ 3^3 = 153）
'''

# def shuixianhua():
#     li = []
#     sum = 0
#     for i in range(100,1000):
#         for j in str(i):
#             sum += int(j)**3
#         if sum == int(i):
#             li.append(i)
#         sum = 0
#     print(li)
# shuixianhua()

'''
7 编程求s=1!+2!+3!+…..+n!
'''

# def s_jiecheng(n):
#     jiec = 1
#     s = 0
#     for i in range(1,n+1):
#         jiec *= i
#         s += jiec
#     print(s)
# s_jiecheng(4)

'''
8 钞票换硬币 把一元钞票换成一分、二分、五分硬币（每种至少一枚），有多种换法，分 别有哪些？
'''

# def n_chaopiao():
#     q = 100-1-2-5
#     li = []
#     count = 0
#     for x in range(int(q/1)):
#         for y in range(int(q/2)):
#             for z in range(int(q/5)):
#                 if (x*1+y*2+z*5) == q:
#                     li.append((x,y,z))
#                     count += 1
#     print(li)
#     print(count)
# n_chaopiao()

'''
9 自己实现在一句话中查找某个单词的算法，存在返回索引号，否则返回False
'''

# def print_find_word(stra, strb):
#     length = len(strb)
#     for i in range(len(stra)):
#         a = stra[i:i + length]
#         if a == strb:
#             print(i)
#     return False
#
# print_find_word('asdfghj', 'fgh')

'''
10 读入一个十进制整数，实现十进制转二进制算法将其转成二进制数 要求：不能使用现成进制转换函数，自己写代码实现
'''

# def shizhuaner_jinzhi(n):
#     str1 = ''
#     num = n
#     while num > 0:
#         str1 += str(int(num%2))
#         num = int(num/2)
#     print(str1[::-1])
# shizhuaner_jinzhi(3)

'''
11 读入一组数字，然后把每组数字加1后输出，比如 123，输出234
'''

# def yizu_num(n):
#     li = []
#     for i in range(len(n)):
#         li.append(n[i]+1)
#     print(li)
# yizu_num([5,4,3])

'''
12 随机生成10位密码 包含大小写、数字
'''

# import random
# import string
# def print_lower_upper_digit():
#     num_lower = list(string.ascii_lowercase)
#     random.shuffle(num_lower)
#     num_upper = list(string.ascii_uppercase)
#     random.shuffle(num_upper)
#     num_digit = list(string.digits)
#     random.shuffle(num_digit)
#     num_num = ''.join(num_lower[:4]+num_upper[:4]+num_digit[:4])
#     print(num_num)
# print_lower_upper_digit()

'''
13 删除一个字符串中的小写字母（map）
'''

# def shanchu_zimu(s):
#     str1 = ''
#     for i in s:
#         asd = False
#         for y in range(ord('a'), ord('z') + 1):
#             if i == chr(y):
#                 asd = True
#         if not asd:
#             str1 += i
#     return str1
# print(shanchu_zimu('a1.,./[bS2Fb3'))

# def shanchu_zimu(s):
#     new = ""
#     b = "abcdefghijklmnopqrstuvwxyz"
#     for c in s:
#         if c not in b:
#             new = new + c
#     return new
# print(shanchu_zimu('a1b2c'))

# def shanchu_zimu(s):
#     new = ""
#     b = "abcdefghijklmnopqrstuvwxyz"
#     for c in s:
#         is_lower = False
#         for x in b:
#             if x == c:
#                 is_lower = True
#                 break
#         if not is_lower:
#             new = new + c
#     return new
#
# print(shanchu_zimu('a1b2c'))

# def shanchu_zimu(s):
#     new = ""
#     for c in s:
#         is_lower = False
#         for x in range(ord('a'), ord('z') + 1):
#             if chr(x) == c:
#                 is_lower = True
#                 break
#         if not is_lower:
#             new = new + c
#     return new
#
# print(shanchu_zimu('a1b2c'))

'''
14 大于5的数字输出（filter）
'''

# def dayuwu_filter(x):
#     return x > 5
#
# num = filter(dayuwu_filter,[1,2,3,4,5,6,7,8,9])
# print(list(num))

'''
15 找到列表中第二大的数，可以用多种方法解决
思路：
找到最大的删除掉，再找最大的
排好序找倒数第二个
遍历，声明两个变量，一个存最大的，一个存第二大的，然后逐一对比
'''

#第一种
# def find_nextwonum(l):
#     for i in l:
#         if i is max(l):
#             l.remove(i)
#     print(max(l))
# find_nextwonum([1,2,3,4,5,6])

#第二种,排序法
# def find_nextwonum2(x):
#     for i in range(int(len(x))):
#         for j in range(i):
#             if x[i] > x[j]:
#                 x[i],x[j] = x[j],x[i]
#     print(x[1])
# find_nextwonum2([1,2,3,4,5,6])
