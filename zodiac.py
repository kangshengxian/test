# zodiac_name=(u'魔羯座',u'水瓶座',u'双鱼座',u'白羊座',u'金牛座',u'双子座',
#            u'巨蟹座',u'狮子座',u'处女座',u'天枰座',u'天蝎座',u'射手座',)
# zodiac_days=((1,20),(2,19),(3,21),(4,21),(5,21),(6,22),
#           (7,23),(8,23),(9,23),(10,223),(11,23),(12,23))
# (month,day)=(2,15)
# zodiac_day=filter(lambda x:x<(month,day),zodiac_days)
# zodiac_len=len(list(zodiac_day)) %12
# print(zodiac_name[zodiac_len])

# a_list=['abc','xyz'] #列表元素
# a_list.append('X') #增加列表元素
# print(a_list) #输出列表元素
# a_list.remove('xyz') #删除列表元素
# print(a_list)

# 练习一 条件语句的使用
# 使用if语句判断字符串的长度是否等于10，根据判断结果进行不同的输出
# 提示用户输入一个1-40之间的数字，使用if语句根据输入数字的大小进行判断，如果输入的数字在 1-10，11-20，21-30，31-40，分别进行不同的输出
# 练习二 循环语句的使用
# 使用for语句输出1-100之间的所有偶数
# 使用while语句输出1-100之间能够被3整除的数字

# a = '12345678911'
# if len(a)==10:
#     print('长度为10')
# else:
#     print('长度不为10')

# num1 = int(input('请输入一个1-40之间的整数：'))
# if 0 < num1 <11:
#     print('该数在1-10之间')
# if 11 < num1 <20:
#     print('该数在11-20之间')
# if 21 < num1 <30:
#     print('该数在21-30之间')
# if 31 < num1 <40:
#     print('该数在31-40之间')


# for i in range(0,101):
#     if i%2 == 0:
#         print(i)

import re
phone = '123-456-789 # 这是电话号码'
p2 = re.sub(r'#.*','',phone)
print(p2)