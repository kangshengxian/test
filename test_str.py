# #练习一 定义字符串
# t1 = 'hello Python'
# print(t1)
#
# t2 = "Let's go!"
# print(t2)
#
# t3 = '"The Zen of Python" --by Tim Peters'
# print(t3)

#练习二
#定义两个字符串分别为 xyz 、abc
# t1 = 'xyz'
# t2 = 'abc'
#对两个字符串进行连接
# print(t1 + t2)

#取出xyz字符串的第二个和第三个元素
# print(t1[1:3])

#对abc输出10次
# print(t2 * 10)

#判断a字符（串）在 xyz 和 abc 两个字符串中是否存在，并进行输出
# print('a' in t1)
# print('b' in t2)

#练习三 列表的基本操作
#定义一个含有5个数字的列表
# alist = ['1','2','3','4','5']
# 为列表增加一个元素 100
# alist.append('100')
# print(alist)
# 使用remove()删除一个元素后观察列表的变化
# alist.remove('2')
# print(alist)
# 使用切片操作分别取出列表的前三个元素，取出列表的最后一个元素
# print(alist[0:3])
# print(alist[-1])

#练习四 元组的基本操作
t1 = ((1,2),(3,4),(5,6))

print('元组中倒数第二个元素为:'+ str(t1[-2]))

t2 = ((1,11),(1,22),(1,23))

print('连接后的元组为:'+ str(t1+t2)+'\n元组元素的个数为:'+str(len(t1 + t2))+ '个')
