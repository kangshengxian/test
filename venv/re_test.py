# import re
# p = re.compile('\d*')
# a=re.findall('\d*','123-456-789')
# print(a)
# print(p.match('123-456-789'))



a=[1,2,3,4,5,6,7]

b=[1,9,25,49]
print(b)

c = []
for i in a:
    if i%2==1:
        c.append(i*i)
print(c)