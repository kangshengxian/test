# 记录生肖，根据年份来判断生肖
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

# print(chinese_zodiac[0])

year = 2018
print(year % 12)
print(chinese_zodiac[year % 12])
print('牛' not in chinese_zodiac)
print(chinese_zodiac + chinese_zodiac[0:4])
