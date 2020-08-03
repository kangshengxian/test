# 题目:有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数?都是多少？
# a=0
# b=[]
# for x in range(1,5):
#     for y in range(1,5):
#         for z in range(1,5):
#             if x!=y and y!=z and z!=x:
#                 res = x*100 + y*10 + z
#                 b.append(res)
#                 a+=1
# print(b,a)

# 题目:企业发放的奖金根据利润提成。利润(I):
# 低于或等于10万元时，奖金可提10%;
# .高于10万元，低于20万元时，
# 低于10万元的部分按10%提成
# 高于10万元的部分，可提成7.5%;
# 20万到40万之间时，高于20万元的部分，可提成5%;
# 40万到60万之间时，高于40万元的部分，可提成3%;
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数?

# lirun_a = int(input('请输入当月利润：'))
# if lirun_a <= 100000:
#     print('应发奖金：',lirun_a*0.1)
# if 200000 >lirun_a > 100000:
#     print('应发奖金：', lirun_a * 0.075)
# if 400000 > lirun_a > 200000:
#     print('应发奖金：', lirun_a * 0.05)
# if 600000 > lirun_a > 400000:
#     print('应发奖金：', lirun_a * 0.03)
# if 1000000 > lirun_a > 600000:
#     print('应发奖金：', lirun_a * 0.015)
# if lirun_a > 1000000:
#     print('应发奖金：', lirun_a * 0.01)


# 题目:一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少?  （a+b）²=a²﹢2ab+b²

# import math
# for i in range(-100,10000):
#     x = int(math.sqrt(i + 100))     # math.sqrt(i + 100)　　返回i + 100的平方根
#     y = int(math.sqrt(i + 268))
#     if (x * x == i + 100) and (y * y == i + 268):
#         print(i)

# 题目;输入某年某月某日，判断这一-天是这一-年的第几天?

# year = int(input('请输入年份'))
# month = int(input('请输入月份'))
# day = int(input('请输入日期'))
# print('{} 月 {} 日 是 {} 年的第 {} 天'.format(month,day,year,(month-1)*30+day))

# 题目:输出9*9口诀表。

# for x in range(1,10):
#     line = ''
#     for y in range(1,x+1):
#         res = ('%s*%s=%s' %(x,y,x*y))
#         line = line + ' ' +res
#     print(line)


# 题目:打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立
# 方和等于该数本身。例如: 153 是一个“水仙花数”，因为153=1的三次方+5的三次方+3的三次方。

# for x in range(1,1000):
#     for y in range(1,1000):
#         for z in range(1,1000):
#             if (x*x*x)+(y*y*y)+(z*z*z) == (x*100+y*10+z):
#                 print(x*100+y*10+z)





# 题目: 一球从100米高度自由落下，每次落地后反跳回原高度的一半;再落下，求它在
# 第10次落地时，共经过多少米?第10次反弹多高?

# a=[100]
# sum=0
# for i in range(10):#计算反弹并插入a列表中
#     x=a[i]/2
#     a.append(x)
#     print("第 %d 次落地！反弹 %f 米！"%(i+1,x))
# for i in a[0:-1]:#计算到第10次落地时的总路程
#     sum+=i*2
# print("共经过%f米！"%(sum-100))
# print("第十次反弹 %f 米！"%a[-1])




'''
一家商场在降价促销。如果购买金额50-100元（包含50元和100元）之间，
会给10%的折扣，如果购买金额大于100元会给20%折扣。编写一程序，
询问购买价格，再显示出折扣（10%或20%）和最终价格
'''

# def print_zekou():
#     aount = int(input("请输入你购买的金额："))
#     if aount < 50:
#         print("不好意思你购买的金额没有折扣,需要支付的金额为：",aount)
#
#     if aount >= 50 and aount <= 100:
#         print(r"你购买的金额为 %d,折扣为：%d,需要支付的金额为%0.2f"%(aount,9,aount*0.9))
#     if aount > 100:
#         print(r"你购买的金额为 %d,折扣为：%d,需要支付的金额为%0.2f"%(aount,8,aount*0.80))
# print_zekou()


'''
求1 + 2 + 3 +….+100
'''
# def print_num_yibai():
#     num = 0
#     for i in range(1,101):
#         num = num + i
#     print("1 + 2 + 3 +….+100=",num)
# print_num_yibai()


'''
判断一个数n能否同时被3和5整除
'''

# def test1():
#     num = int(input('请输入n的值：'))
#     if num == 0:
#         print('除数不能为0')
#         return 0
#     if num%3==0 and num%5==0:
#         print('n的值 %s 能同时被3和5整除' %num)
#     else:
#         print('n的值 %s 不能同时被3和5整除' % num)
# test1()

'''
一个足球队在寻找年龄在10到12岁的小女孩（包括10岁和12岁）加入。
编写一个程序，询问用户的性别（m表示男性， f表示女性）和年龄，
然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数
'''

# def test2():
#     count = 0
#     for i in range(10):
#
#         sex = input('请输入性别，（m表示男性， f表示女性）：')
#         if sex == 'f':
#             age = int(input('请输入年龄：'))
#             if 12>=age>=10:
#                 print('您可以加入球队!')
#                 count += 1
#         else:
#             print('您不能加入球队！')
#     print('满足条件总人数为:',count)
# test2()


'''
长途旅行中，刚到一个加油站，距下一个加油站还有200km，而且以后每个加油站之间距离都是200km。
编写一个程序确定是不是需要在这里加油，还是可以等到接下来的第几个加油站再加油
'''

# def print_km():
#     youxiang = int(input("你的油箱多大？，单位升："))
#     shxia = float(input("目前你的油箱还有多少油，按百分比，比如一半就是0.5："))
#     lucheng = int(input("你的车每升油能走多远："))
#     syou = (youxiang*shxia-5)*lucheng
#     if syou < 200:
#         print("在当前的加油站要加油")
#     else:
#         print("第%d个加油站加油"%(syou/200))
# print_km()


'''
现有面包、热狗、番茄酱、芥末酱以及洋葱，数字显示有多少种订购组合，其中面包必订，0不订，1订，比如10000，表示只订购面包
'''

def print_ding():
    count = 0
    for a in '1':
        for b in '01':
            for c in '01':
                for d in '01':
                    print(a+b+c+d)
                    count += 1
    print("有%d种组合"%count)
print_ding()