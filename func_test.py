# list1 = [1,2,3]
# it = iter(list1)
# print(next(it))

# def frange(start,stop,step):
#     x = start
#     while x < stop:
#         yield x
#         x += step
#
# i = frange(10,20,0.5)
# print(next(i))
# print(next(i))


# for i in frange(10,20,0.5):
#         print(i)

# def add(a,b):
#     return a+b
func2 = lambda item:item[1]
def func2(item):
    return item[1]
adict = {'a':'cc','b':'dd'}
for i in adict.items():
    print(func2(i))

# a = [1,2,3,4,5,6,7]
# print(list(filter(lambda x:x>2 , a)))

# zip((1,2,3),(4,5,6))
# for i in zip((1,2,3),(4,5,6)):
#     print(i)

# def func3():
#     a = 1
#     b = 2
#     print(a + b)
# func3()
#
#
# def func(a):
#     def add(b):
#         return a + b
#     return add
# func(2)
