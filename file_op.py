#将小说的主要人物记录在文件中
#写入人物名称到文件
# file1 = open('name.text','w',encoding='utf-8')
# file1.write('诸葛亮')
# file1.close()
# 读取文件人物名称
# file2 = open('name.text',encoding='utf-8')
# print(file2.read())
# file2.close()
#写入人物名称到文件
# file3 = open('name.text','a',encoding='utf-8')
# file3.write('刘备')
# file3.close()
# #读取文件单行名称
# file4 = open('name.text',encoding='utf-8')
# print(file4.readline())
# #
# file5 = open('name.text',encoding='utf-8')
# for line in file5.readlines():
#     print(line)
#     print('=====')

# file6 = open('name.text',encoding='utf-8')
# print(file6.tell())
# file6.read(1)
# print(file6.tell())

# a = 123
# try:
#     a.append()
# except AttributeError:
#     print('整型没有append属性~')

def fun1() :
    n1 = int(input('请输入第一个整数：'))
    n2 = int(input('请输入第二个整数：'))
    print('%s * %s = %s' %(n1,n2,n1*n2))

fun1()
# def fun2() :
#     n_num = input("请输入多个整数：")
#     n_list = n_num.split(',')
#     s = 0
#     for i in range(len(n_list)):
#         s+=int(n_list[i])
#     print("这些数字和为：%s" %(s))
# fun2()

# def fun2(*nums) :
#     print('其中最大值为：%s' %max(list(nums)))
#     print('其中最小值为：%s' %min(list(nums)))
# fun2(1,3,5,7,33,44)

# def fun3(n):
#     x=1
#     for i in range(1,n+1):
#         x=i*x
#     return x
# print(fun3(3))

# 创建一个文件，并写入当前日期
# 再次打开这个文件，读取文件的前4个字符后退出
# file1 = open('date.txt','w',encoding='utf-8')
# file1.write('2020/7/18')
# file1.close()
#
# file2 = open('date.txt',encoding='utf-8')
# print(file2.read(4))
# file2.close()

# a = open('name.txt',encoding='utf-8')
# data = a.read()
# data2 = data.split('fdsgsdfgdsf')
# print(data)

# b = open('sanguo.txt',encoding='utf-8')
# print(b.read().replace('\n',''))

# print(open('name.txt',encoding='utf-8').read())