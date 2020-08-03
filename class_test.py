# class Player():              #定义一个类
#     def __init__(self,name,hp,accu):
#         self.name = name
#         self.hp = hp
#         self.accu = accu
#     def print_role(self):    #定义一个方法
#         print('%s %s %s' %(self.name,self.hp,self.accu))
#
#     def updatename(self,name):
#         self.name = name
#
# user1 = Player('tom',100,'war')    #类的实例化
# user2 = Player('jerry',90,'master')
# user1.print_role()
# user2.print_role()
#
# user2.updatename('aaa')
# user2.print_role()

# class xuesheng:
#     def __init__(self,yuwen):
#         self.yuwen = yuwen
#     def get_chengji(self):
#         print(self.yuwen)
# a = xuesheng(100)
# b = xuesheng(20)
#
# print(a.yuwen)
# a.get_chengji()


# class people:
#     def __init__(self,sex,age):
#         self.sex = sex
#         self.age = age
#     def print_p(self):
#         print('性别：%s 年龄：%s' %(self.sex,self.age))
# a = people('boy','20')
# b = people('girl','18')
# a.print_p()
# b.print_p()



class Monster():
    '定义怪物类'
    def __init__(self,hp=100):
        self.hp = hp
    def run(self):
        print('移动到某个位置')

    def whoami(self):
        print('我是怪物父类')
class Animals(Monster):
    '普通怪物'
    def __init__(self,hp=10):
        super().__init__(hp)
class Boss(Monster):
    'Boss类怪物'
    def __init__(self,hp=1000):
        super().__init__(hp) #不用重新初始化
    def whoami(self):
        print('我是怪物我怕谁')

a1 = Animals(1)
print(a1.hp)
print(a1.run())
a2 = Boss(800)
print(a2.hp)
a2.whoami()
a3 = Monster()
print(isinstance(a2,Monster))