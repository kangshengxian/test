import re

phone = '182-7048-5529 康先生'
t1 = re.sub(r'康.*$','',phone)
print(t1)
