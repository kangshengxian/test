chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
zodiac_name = (u'魔羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
               u'巨蟹座', u'狮子座', u'处女座', u'天枰座', u'天蝎座', u'射手座',)
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 223), (11, 23), (12, 23))

cz_num = {i: 0 for i in chinese_zodiac}

z_num = {i: 0 for i in zodiac_name}

while True:

    #用户输入月份和日期
    year=int(input('请输入年份'))
    month = int(input('请输入月份'))
    day = int(input('请输入日期'))

    n = 0
    while zodiac_days[n] < (month,day):
        if month == 12 and day > 23:
            break
        n += 1
        #输出星座和生肖
    print(zodiac_name[n])
    print('%s 年的生肖是 %s' %(year,chinese_zodiac[year%12]))

    cz_num[chinese_zodiac[year %12]] += 1
    z_num[zodiac_name[n]] +=1

    # 输出生肖和星座的统计信息
    for each_key in cz_num.keys():
        print('生肖 %s 有 %d 个' %(each_key,cz_num[each_key]))
    for each_key in z_num.keys():
        print('星座 %s 有 %d 个' %(each_key,z_num[each_key]))

# for zd_num in range(len(zodiac_days)):
#     if zodiac_days[zd_num] >=(int_month,int_day):
#         print(zodiac_name[zd_num])
#         break
#     elif int_month == 12 and int_day>23:
#         print(zodiac_name[0])
#         break

# print(type(str_month))
#
# zodiac_day=filter(lambda x:x<=(month,day),zodiac_days)
# zodiac_len=len(list(zodiac_day))%12
# print(zodiac_name[zodiac_len])
