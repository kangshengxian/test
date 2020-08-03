# # 求一个数的阶乘
# def test():
#     a = 1
#     num = int(input('请输入一个数'))
#
#     for i in range(1,num+1):
#         a = a*i
#
#     print('从1到',num,'阶乘和为',sum)
# test()


'''
现有面包、热狗、番茄酱、芥末酱以及洋葱，数字显示有多少种订购组合，其中面包必订，0不订，1订，比如10000，表示只订购面包
'''
# count = 0
# for a in '1':
#     for b in '01':
#         for c in '01':
#             for d in '01':
#                 for e in '01':
#                     print(a+b+c+d+e)
#                     count += 1
# print("有%d种组合"%count)


'''
基于上题：给出每种食物的卡路里（自定义），再计算出每种组合总共的卡路里
'''

count = 0
for a in '1':
    for b in '01':
        for c in '01':
            for d in '01':
                for e in '01':
                    print(a+b+c+d+e,"这种组合的卡路里为", int(a) * 100 + int(b) * 200 + int(c) * 300 + int(d) * 400 + int(e) * 500)
                    count += 1
print("有%d种组合"%count)


