# 在Python程序中，分别使用未定义变量、访问列表不存在的索引、访问字典不存在的关键字观察系统提示的错误信息
# 通过Python程序产生IndexError，并用try捕获异常处理

# list1 = [1,2,3,4]
# # print(list1[4])
#
# dict1 = {'a':1,'b':2}
# # print(dict1['c'])
#
# try:
#     a = [1,2,3,4]
#     print(list1[4])
#     print(dict1['c'])
# except:
#     print('索引错误')
#
#
# try:
#     print(1/0)
# except:
#     print('错误')

#定义一个错误信息
# try:
#     raise NameError('helloError')
# except:
#     print('my custom error')


try:
    a = open('name.text')
except Exception as e:
    print(e)
finally:
    a.close()


