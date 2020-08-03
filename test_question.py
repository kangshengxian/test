'''
第 7题 用户输入不同的数据，当输入的数据达到3个数字的时候，求和结束程序。（数字可以是整数）
提示：判断是否整数的方法，isdigit()
遍历所有的输入数据，判断是否在0-9的字符串范围内
'''

# def different_type():
#     count = 1
#     sum = 0
#     while count <= 3:
#         num = input('请输入不同的数据：')
#         if num.isdigit():               #怎么判断浮点数
#             count += 1
#             sum += int(num)
#     print('和为：',sum)
# different_type()


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
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
july 31st,2020 question
'''



