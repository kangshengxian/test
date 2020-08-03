# 从1到10 所有偶数的平方
# alist=[]
# for i in range(1,11):
#     if (i % 2 == 0):
#         alist.append(i*i)
#
# print(alist)

# blist=[i*i for i in range(1,11) if(i % 2) == 0]
# print(blist)

# z_num={}
# for i in zodiac_name:
#     z_num[i] = 0

# b_num={i:0 for i in z_num}

# a=(1,3,5,7,9)
# b = 4
# c = filter(lambda x:x<b,a)
# print(list(c))


# n = 100
#
# sum = 0
# counter = 1
# while counter <= 100:
#     sum = sum + counter
#     counter += 1
#
# print("1 到 %d 之和为: %d" % (n, sum))

# var = 1
# while var == 1:  # 表达式永远为 true
#     num = int(input("输入一个数字  :"))
#     print("你输入的数字是: ", num)
#
# print("Good bye!")

count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")