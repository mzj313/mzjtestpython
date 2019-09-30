from test.mymodule import Hero


class User:
    def __init__(self, id, name=''):
        self.id = id
        self.name = name

    def run(self):
        print(self.to_str() + " is running..")

    def set_name(self, name):
        self.name = name

    def to_str(self):
        return str(self.id) + "_" + self.name


user1 = User(1)
print(str(user1) + " id=" + str(user1.id) + ",name=" + user1.name)
user1.set_name("li4")
print(str(user1) + " id=" + str(user1.id) + ",name=" + user1.name)
user1.run()

# 继承
class Teacher(User):
    def __init__(self, id, name, school):
        super().__init__(id, name)
        self.school = school

    def teach(self):
        print(self.to_str() + " is teaching..")

    # 重写父类方法
    def to_str(self):
        return str(self.id) + "_" + self.name + "_" + self.school


teacher1 = Teacher(2, "wang5", "xx小学")
teacher1.teach()
teacher1.run()

# 引用其他模块的类
hero = Hero("ma6")
hero.fight()

# 标准库
from collections import OrderedDict

addrs = OrderedDict()
addrs['li4'] = 'hebei'
addrs['wang5'] = 'henan'
addrs['ma6'] = 'beijing'

print(addrs)
