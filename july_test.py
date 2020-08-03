'''
第 1 题，输出九九乘法表
'''

'''
自己写的
'''
# def test1():
    # for i in range(1, 10):
    #
    #     for j in range(1, i + 1):
    #         print("%d*%d=%d" % (j, i, i * j),end=' ')
    #
    #     print()    #打印回车
# test1()

'''
答案参考
'''
# for i in range(1, 10):
#
#     for j in range(1, i + 1):
#         print("%d*%d=%d" % (j, i, i * j), end="\t")
#
#     print()


'''
第  2 题，有 1 2 3 4 这四个数字，能组成多少个互相不同且无重复数字的 3 位数，分别是什么。

思路：要组成几位数，就用几个for循环，无论给了几个数字，全部放进列表，都不用改代码。
'''

'''
自己写的
'''
# def test2():
#     a = []
#     c = 0
#     for x in range(1,5):
#         for y in range(1, 5):
#             for z in range(1, 5):
#                 if x!=y and y!=z and z!=x:
#                     c = c + 1
#                     b = x*100 + y*10 + z
#                     a.append(b)
#     print(a,'共有%s个数字无重复的3位数' %c)
# test2()

'''
答案参考
'''
# count = 0
# m = [1, 2, 3, 4]
# for a in m:
#     for b in m:
#         for c in m:
#             if a != b and b != c and a != c:
#                 count += 1
#                 print(a, b, c)
# print()
# print("能组成%d 个不相同且无重复的3位数" % count)


'''
第  3 题，跟电脑玩剪刀石头布游戏，一直循环玩，可手动退出，不玩了就计算玩家胜率
'''

'''
自己写的
'''
# def test3():
    # count = 0
    # winr = 0
    # from random import randint
    # while True:
    #     print('开始游戏↓↓↓')
    #     player = int(input('1代表石头 2代表剪刀 3代表布 0退出,请输入：'))
    #     if player == 0:
    #         print('游戏结束！')
    #         print('你的胜率是：',winr/count*100)
    #         break
    #     elif player>3:
    #         print('请输入1-3之间的数')
    #         continue
    #     computer = randint(1, 3)   ##随机生成一个1-3的数
    #     count = count + 1
    #     print('电脑出的是', computer)
    #     if player == computer - 1 or player == computer + 2:
    #         print('你赢了！')
    #         winr += 1
    #     elif player == computer:
    #         print('平局，再来一次！')
    #     else:
    #         print('你输了！')
# test3()

'''
答案参考
'''
# def play_game():
#     # 总把数
#     count = 0
#     # 胜率把数
#     player_win = 0
#
#     while True:
#         import random
#         computer = random.randint(1, 3)
#         player = int(input("请输入数字，1剪刀，2石头，3布,0手动退出："))
#
#         # 手动退出游戏
#         if player == 0:
#
#             # 判断一次没玩就退出游戏
#             if count == 0:
#                 print("您还没开始游戏!!!")
#                 break
#
#             print("游戏结束!!!")
#             print("玩家玩了:%d把，赢了:%d把，胜率:%.2f%%" % (count, player_win, player_win / count * 100))
#             break
#
#         # elif player < 1 or player > 3:
#         elif player not in (1, 2, 3):
#             print("请输入1-3之间的数字")
#             # 增加换行，美化显示效果
#             print()
#             continue
#
#         # 把数计数
#         count += 1
#
#         print("电脑出拳为：%d" % computer)
#         if player == computer - 1 or player == computer + 2:
#             print("玩家胜利！")
#
#             # 玩家胜利计数
#             player_win += 1
#
#         elif player == computer:
#             print("平局！")
#         else:
#             print("电脑胜利")
#
#         print()
#
# play_game()


'''
第  4 题，寻找15到20岁的女孩子当拉拉队员，询问，符合要求输出加入成功，询问10次后，输出满足条件总人数
'''

'''
自己写的
'''
# def test4():
    # count = 0
    # for i in range(10):
    #     age = int(input('请输入年龄：'))
    #     if 20>=age>=15:
    #         sex = input('请输入性别：')
    #         if sex == '女':
    #             print('加入成功！')
    #             count += 1
    #         else:
    #             print('您不符合要求！')
    #     else:
    #         print('您不符合要求！')
    # print('满足条件总人数为',count)
# test4()


'''
第  5 题，利用 for 循环给列表  ls = [1,7,4,89,34,2,100,0] 从小到大排序，==>冒泡排序法
思路：先取列表的第一个数字，依次跟后面的数字比较大小，如果第一个数字比后面的大，则交换位置。
利用下标来取值，第一个数字a依次从 第一位取到倒数第一位（把最后一位留给第二个数字b来取，好做比较）
第二个数字b依次从第二位取到最后一位。以此类推，当把列表中数字取完，结果就出来了。

'''

'''
自己写的
'''
# def test5():
#     a = [1, 7, 4, 89, 34, 2, 100, 0]
#     for i in range(len(a)-1):
#         for j in range(i+1, len(a)):
#             if a[i] > a[j]:
#                 a[i], a[j] = a[j], a[i]
#     print(a)
#
# test5()



'''
第 6题
现有面包、热狗、番茄酱、芥末酱以及洋葱，数字显示有多少种订购组合，其中面包必订，0不订，1订，比如10000，表示只订购面包
'''

# def group():
#     count = 0
#     for a in '1':
#         for b in '01':
#             for c in '01':
#                 for d in '01':
#                     for e in '01':
#                         count += 1
#                         print(a+b+c+d+e)
#     print('有 %s 种组合' %count)
#
# group()

'''
基于上题：给出每种食物的卡路里（自定义），再计算出每种组合总共的卡路里
'''
# def group():
#     count = 0
#     for a in '1':
#         for b in '01':
#             for c in '01':
#                 for d in '01':
#                     for e in '01':
#                         count += 1
#                         print(a+b+c+d+e,"不同组合的卡路里为", int(a) * 100 + int(b) * 200 + int(c) * 300 + int(d) * 400 + int(e) * 500)
#     print('有 %s 种组合' %count)
#
# group()


'''
第 7题
实现一个简单的单词本
- 功能：
- 可以添加单词和词义，当所添加的单词已存在，让用户知道；
- 可以查找单词，当查找的单词不存在时，让用户知道；
- 可以删除单词，当删除的单词不存在时，让用户知道；
- 以上功能可以无限制操作，直到用户输入bye退出程序。

'''

# def netbook():
#     dict1 = {}
#     while True:
#         op = input('请输入要进行的操作（添加:add 查找:select 删除:delete 打印单词本:print 退出程序:bye）：')
#         if op == 'add':
#             word_add = input('请输入要添加的单词：')
#             if word_add in dict1.keys():
#                 print('您输入的单词已存在！')
#                 continue
#             else:
#                 ciyi_add = input('请输入单词词义：')
#             dict1[word_add] = ciyi_add
#         if op == 'select':
#             word_select = input('请输入要查找的单词：')
#             if word_select not in dict1.keys():
#                 print('您要查找的单词不存在！')
#                 continue
#             else:
#                 print('它的词义为：',dict1[word_select])
#         if op == 'delete':
#             word_delete = input('请输入要删除的单词：')
#             if word_delete not in dict1.keys():
#                 print('您要删除的单词不存在！')
#             else:
#                 print('删除成功！')
#         if op == 'bye':
#             print('程序已退出！')
#             break
#         if op != 'add' and op != 'select' and op != 'delete' and op != 'bye' and op != 'print':
#             print('您输入的格式错误，请重新输入！')
# netbook()


'''
第 8题
输入一个正整数，输出其阶乘结果

'''

# def jiec():
#     c = 1
#     num = int(input('请输入一个正整数：'))
#     for i in range(1,num + 1):
#         c = c * i
#     print(c)
# jiec()

'''
第 9题
输入3个数字，以逗号隔开，输出其中最大的数
'''
# def max():
#
#     num = input('请输入3个数，以‘,’隔开：')
#     nums = num.split(',')
#     numss = int(nums[0])
#     for i in nums:
#         if numss < int(i):
#             numss = int(i)
#     print(numss)
#
# max()


'''
第 10题
输入一个年份，输出是否为闰年
是闰年的条件：
能被4整数但不能被100整除，或者能被400整除的年份都是闰年
'''

# def leap_year():
#
#     year = int(input('请输入年份：'))
#     if (year %4 == 0 and year %100 != 0) or year %400 == 0:
#         print(year,'是闰年')
#     else:
#         print(year,'不是闰年')
# leap_year()


'''
习题1：设定一个用户名和密码，用户输入正确的用户名和密码，则显示登录成功，否则提示登录失败，用户最多失败3次，否则退出程序。
提示：使用while或者for来限定重试的次数，使用input获取用户输入使用 ==判断用户的用户名和密码。
'''
# def user_wel():
#     count = 1
#     c = 3
#     print('用户最多失败3次！')
#     while count <= 3:
#         user = 'kang'
#         password = '123'
#         d_user = input('请输入用户名：')
#         d_password = input('请输入密码：')
#         if d_user == user and d_password == password:
#             print('登陆成功！')
#         else:
#             print('登录失败，请重新输入！')
#             count += 1
#             c -= 1
#             print('您还有 %s 有机会！' %c)
#         if count > 3:
#             print('由于失败3次，退出程序！')
# user_wel()


'''
习题2：自己实现一个函数，在一句话中查找某个单词的算法，存在返回索引号，否则返回False
提示：使用句子中的坐标遍历句子的每一个位置，使用查找单词的长度结合使用切片来查找单词。例如：s[i:i+len(单词)]
'''


# def find_word(word,num):
#     for i in range(len(word)):
#         #print(i)
#         #print(word[i:len(num)+i])
#         if len(word[i:]) <= len(num):
#             print("没有找到！！")
#             return 0
#         elif word[i:len(num)+i] == num:
#             #print(word[i:len(num)-1])
#             print("索引：",i+1)
#             return 1
# find_word('how are you','a')


'''
习题3：随机生成一个整数，1-100之间你最多猜5次，如果猜大了，提示大了小了，提示小了，猜对了，提示猜中。5次都没猜中，就猜没猜中。
'''

# def int_num():
#     import random
#     count = 1
#     chance = 5
#     num = random.randint(1, 101)
#     while count <= 5:
#         a_num = int(input('请在1-100之间输入要猜的数，您最多猜5次：'))
#
#
#         if a_num > num:
#             print('猜大了！')
#             count += 1
#             chance -= 1
#             print('您还有 %s 次机会！' %chance)
#         elif a_num <num:
#             print('猜小了！')
#             count += 1
#             chance -= 1
#             print('您还有 %s 次机会！' %chance)
#         else:
#             print('猜中了！')
#             break
#         if chance == 0:
#             print('没猜中')
#             print('随机生成数是：', num)
# int_num()

'''
习题4：使用while,计算随机数之和，超过100的时候，停止程序。随机数1-20的范围产生，要求记录一下产生的随机数，以及最后的和，以及随机数的个数。
'''

# def randoem_num():
#     import random
#     sum = 0
#     a = []
#     while sum < 100:
#         num = random.randint(1,21)
#         a.append(num)
#         sum += num
#     print('产生的随机数：', a)
#     print('最后的和为：', sum)
#     print('随机数的个数为：', len(a))
# randoem_num()

'''
习题5：遍历字符串、列表，分别基于位置和和基于字符遍历
'''

# def print_str_list(s):
#     for i in s:
#         print(i)
#     for i in range(len(s)):
#         print(s[i])
# print_str_list('abc')

'''
习题6：遍历一个列表中的嵌套列表和元组的所有元素,将1-12的数字进行输出！[[[1,2,3],4,5],7,8,(9,10,(11,12))]
'''

# def str_typle(s):
#     for i in s:
#         if isinstance(i, (list, tuple)):
#             for j in i:
#                 if isinstance(j, (list, tuple)):
#                     for k in j:
#                         print(k,end=' ')
#                 else:
#                     print(j,end=' ')
#         else:
#             print(i,end= ' ')
# str_typle([[[1,2,3],4,5],7,8,(9,10,(11,12))])

'''
第 1题 判断一个数是否是素数
'''

# def prime_number():
#     n = int(input('请输入：'))
#     if n == 1 or n == 2:
#         print("是素数")
#     for i in range(2, n):
#         if n % i == 0:
#             print("不是素数")
#             break
#         else:
#             print("是素数")
#             break
#
# prime_number()

'''
第 2题 求100以内的素数和
'''

# def prime_sum(n): #1060
#     sum = 0
#     for i in range(1,n+1):
#         if i == 2:
#             sum += i
#         for j in range(2,i):
#             if i % j == 0:
#                 break
#             else:
#                 sum += i
#     print(sum)
#
# prime_sum(100)


'''
第 2题 求100以内的素数和
100以内的质数有2、3、5、7、11、13、17、19、23、29、31、37、41、43、47、53、59、61、67、71、73、79、83、89、97共25个，和为1060
'''
# def all_prime(num):
#
#     lst = []
#     sum = 0
#     if num <= 1:
#         print('0 ~ %d以内没有任何素数' % num)
#     for i in range(2, num+1):
#         for j in range(2, int(i/2)+1):
#             if not i % j:
#                 break
#         else:
#             lst.append(i)
#             sum += i
#     print(lst,sum)
# all_prime(100)

'''
第 3题 使用 for 的方式，求一下100以内奇数之和
'''
#第一种
# def num_sum():
#     sum = 0
#     for i in range(1,101,2):
#         sum += i
#     print(sum)
# num_sum()

# #第二种
# def jishu():
#     s = []
#     sum = 0
#     for i in range(1,101):
#         if i % 2 != 0:
#             s.append(i)
#             sum += i
#     print(s,sum)
# jishu()

'''
第 4题 用户输入多个数字，当输入偶数的时候求和，输入奇数，不求和，输入.（一个点）的时候结束求和，打印求和结果
'''

# def nums_sum():
#     try:
#         sum = 0
#         while True:
#             num = input('输入多个数字，以英文逗号隔开，输完按回车，结束按.：')
#             if num == '.':
#                 print('结束求和！')
#                 break
#             elif int(num) %2 == 0:
#                 sum += int(num)
#     except ValueError as a:
#         print(a)
# nums_sum()


# def print_oushu_qiuhe():
#     try:
#         num_two = 0
#         while True:
#             num_one = input("输入数值，偶数求和，奇数不求和,\".\"结束求和：")
#             if num_one == '.':
#                 print(num_two)
#                 break
#             elif int(num_one)%2 == 0:
#                 num_two += int(num_one)
#     except Exception as e:
#         print(e)
# print_oushu_qiuhe()

'''
第 5题 嵌套循环输出10-50中个位带有1-5的所有数字:
方法1：数字和10取余，判断是否大于0并且小于等于5
方法2：将数字转换为str，取各位的字符判断字符是否在1-5内。
方法3：拼接数字
'''

# def while_num():
#     for i in range(10,51):
#         if i %10 >0 and i %10 <=5:
#             print(i,end=' ')
# while_num()

'''
第 6题 输入3个数字，达到3个数字求和，结束程序
'''

# def print_three_num():
#     try:
#         num_one = 0
#         for i in range(3):
#             num = int(input("请输入数值"))
#             num_one += num
#         print(num_one)
#     except Exception as e:
#         print(e)
# print_three_num()

'''
第 7题 用户输入不同的数据，当输入的数据达到3个数字的时候，求和结束程序。（数字可以是整数）
提示：判断是否整数的方法，isdigit()
遍历所有的输入数据，判断是否在0-9的字符串范围内
'''

def different_type():
    count = 1
    sum = 0
    while count <= 3:
        num = input('请输入不同的数据：')
        if len(num.split('.')) == 2:
            s = num.split('.')
            if s[0].isdigit() and s[1].isdigit():
                num = float(num)
                count += 1
                sum += num
                continue
        if num.isdigit():
            count += 1
            sum += int(num)
    print('和为：',sum)

different_type()

'''
第 8题 用嵌套列表的方式，遍历输出一个矩阵
'''

# def matrix():
#     str = [[1,2,3],[4,5,6],[7,8,9]]
#     for i in str:
#         print(i)
#
# matrix()

'''
第 9题 求以下矩阵四边元素之和
l = [
     [1,2,3,4,5], 
     [1,2,3,4,5], 
     [1,2,3,4,5],
     [1,2,3,4,5],
     [1,2,3,4,5]  
]
'''

# def print_sibinayuansuzhihe():
#     num_list = [[1,2,3,4,5],
#                 [1,2,3,4,5],
#                 [1,2,3,4,5],
#                 [1,2,3,4,5],
#                 [1,2,3,4,5] ]
#     num_one = 0
#     for i in range(len(num_list)):
#         if i == 0 or i == len(num_list)-1:
#             for j in num_list[i]:
#                 num_one += j
#         else:
#             num_one += num_list[i][0] + num_list[i][len(num_list)-1]
#             continue
#     print(num_one)
# print_sibinayuansuzhihe()

'''
第 10题 统计单词中包含字母a的单词个数
'''

# def count_word():
#     count = 0
#     iword = 'sasdf a sa'
#     for i in range(len(iword)):
#         if iword[i] == 'a':
#             count += 1
#     print('字母a有 %s 个' %count)
# count_word()

'''
第 11题 成绩等级判断 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示， 60-89分之间的用B表示，60分以下的用C表示
'''

def chengjidengji():
    while True:
        try:
            result = input('请输入成绩(输0结束程序)：')
            if result.isdigit():
               result = int(result)
            elif len(result.split(".")) == 2:
                s = result.split(".")
                if s[0].isdigit() and s[1].isdigit():
                    result = float(result)
            if result == 0:
                print('程序退出！')
                break
            if result >= 90:
                print('%s分,成绩等级为A！' %result)
            if 89 >= result >= 60:
                print('%s分,成绩等级为B！' %result)
            if result < 60:
                print('%s分,成绩等级为C！' % result)
        except TypeError as a:
            import traceback
            traceback.print_exc()
            # print(a)
            print('你输入的类型不对', a)

chengjidengji()

'''
第 12题 实现数学中多项式求和公式的打印 比如：a6x^6 + a5x^5 + a4x^4 + a3x^3 + a2x^2 + a1x^1 + a0
'''

# def print_duoxiangshi(n):
#     num_str = ''
#     num_list = range(0,n+1)
#     for i in num_list[::-1]:
#         if i ==0:
#             num_str += 'a'+str(i)
#         else:
#             num_str += 'a'+str(i)+'x'+'^'+str(i)+'+'
#     print(num_str)
# print_duoxiangshi(6)

'''
第 13题 统计名字列表中，各名字的首字母在名字列表中出现的次数
'''

# def list_name():
#     a = {}
#     name_str = ['zhangwei','pengyuyan','lubenwei','zhangjie','liuxing']
#     for i in name_str:
#         if i[0] in a.keys():
#             a[i[0]] = a[i[0]] + 1
#         else:
#             a[i[0]] = 1
#     print(a)
# list_name()

'''
第 14题 输入三个数，判断是否能构成三角形 能构成三角形三边关系： 三边都大于零 两边之和大于第三边，两边之差小于第三边
'''

# def sanjiaoxingguanxi():
#     num1 = int(input('请输入第一个数：'))
#     num2 = int(input('请输入第二个数：'))
#     num3 = int(input('请输入第三个数：'))
#     if num1 == 0 or num2 == 0 or num3 == 0:
#         print('其中有数字是0，不能构成三角形！')
#         return 0
#     if not num1 + num2 > num3 and num1 + num3 > num2 and num3 + num2 > num1:
#         print('两边之和小于第三边，不能构成三角形！')
#         return 0
#     if not num1-num2<num3 and num1-num3<num2 and num3-num2<num1:
#         print('两边之差小于第三边，不能构成三角形！')
#         return 0
#     else:
#         print('能构成三角形！')
# sanjiaoxingguanxi()

'''
第 15题 实现字典的fromkeys方法
例如：
seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq, 10)
print "New Dictionary : %s" % str(dict)
结果：New Dictionary : {'age': 10, 'name': 10, 'sex': 10}
'''

# def print_dict_fromkeys(seq,n):
#     num_dict = {}
#     for i in seq:
#         num_dict[i] = n
#     print(num_dict)
# print_dict_fromkeys(('n','a','s'),20)

'''
第 16题 键盘读入一字符串，逆序输出
'''

# def print_nixv():
#     str1 = list(input('请输入一串字符串:'))
#     for i in range(len(str1)-1):
#         for j in range(i+1,len(str1)):
#             if str1[i] < str1[j]:
#                 str1[i],str1[j] = str1[j],str1[i]
#     print(str1)
# print_nixv()

'''
第 17题 读入一个整数n，输出n的阶乘
'''

# def print_factorial(n):
#     c = 1
#     for i in range(1,n+1):
#         c *= i
#     print(c)
# print_factorial(10)

'''
第 18题 打印1/2, 1/3, 1/4,….1/10
'''

# def print_num(a):
#     empty_str = ''
#     alist = range(2,a+1)
#     for i in alist[::+1]:       #序列的翻转操作
#         if i == 10:
#             empty_str += '1' + '/'+str(i)
#         else:
#             empty_str += '1'+'/'+str(i)+', '
#     print(empty_str)
# print_num(10)














'''
------------------------------------------------------------------------------------------------------------------------
'''

'''
通过指定列表中的元素排序来输出列表
结果 排序列表： [(4, 1), (2, 2), (1, 3), (3, 4)]
'''

# 获取列表的第二个元素
# def takeSecond(elem):
#     return elem[1]
#
# # 列表
# random = [(2, 2), (3, 4), (4, 1), (1, 3)]
#
# # 指定第二个元素排序
# random.sort(key=takeSecond)
#
# # 输出类别
# print('排序列表：', random)


# list1 = ['Google', 'Runoob', 'Taobao']
# list1.pop()
# print ("列表现在为 : ", list1)
# list1.pop(1)
# print ("列表现在为 : ", list1)

# 创建元组(不要括号也可以)
# a = 1,2,3,4,5
# b = ()
# print(type(a))
# print(type(b))

# tup1 = ('Google', 'Runoob', 1997, 2000)
# tup2 = (1, 2, 3, 4, 5, 6, 7)
# list1 = [1,2,3,4,5,6,7]
# print("tup1[]: ", tup1[0])
# print("tup2[]: ", tup2[1:7])
# print('list1[]', list1[1:6])

# tup1 = (12, 34.56)
# tup2 = ('abc', 'xyz')
#
# # 以下修改元组元素操作是非法的。
# # tup1[0] = 100
#
# # 创建一个新的元组
# tup3 = tup1 + tup2
# print(tup3)


# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# a = str(dict)
# print(a)
# print(type(a))


# confusion = {}
# confusion[1] = 1
# confusion['1'] = 2
# confusion[1] += 1    ## 给Key为1的value值加1
#
# sum = 0
# for k in confusion:
#     sum += confusion[k]
#
# print(sum)