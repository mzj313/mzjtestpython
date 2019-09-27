# import test.mymodule as m
from test import mymodule
# from test.mymodule import print_all
# import * 可能产生覆盖
# from test.mymodule import *


def add_user(name, phones, age='', gender='male'):
    """
    带默认值的参数应该放到后面；禁止修改列表，而应该创建副本
    增加用户
    """
    user = {}
    print("add user.. name" + name + ",age=" + str(age) + ",gender=" + gender + ",phones=" + str(phones))
    user['name'] = name.title()
    user['age'] = age
    user['gender'] = gender
    user['phones'] = phones
    return user


print(add_user("li4", [], 19, 'female'))
print(add_user(age=22, name="wang5", phones=['18812345678']))
print(add_user("mzj", ['18812345678']))
print('------------------------------------')


def println(size, *params):
    """传递任意数量的实参"""
    print(str(size) + str(params))


println(1, 'a')
println(2, 'a', 1)

# 引用其他模块的函数
# m.print_all('a', 'b')
mymodule.print_all('a', 'b')
# print_all('a', 'b')
# print_all('a', 'b')
# 保留空行
