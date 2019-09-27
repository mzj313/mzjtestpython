# 变量和类型
message = "Hello," + " mzj ".strip() + "! "
print(message)
print("2的立方=" + str(2 ** 3))
print("0.1+0.2=" + str(0.1 + 0.2))
print(3/2)
print(3.0/2)
num = '22'
num = int(num)
print(num >= 20)
print('列表------------------------------------')
arr = ['lee1', 'li4', 'wang5']
print("初始.. " + str(arr) + " 长度=" + str(len(arr)) + " " + arr[0] + " " + arr[1].title() + " " + arr[-1])
arr[0] = 'lee2'
print('replace [0].. ' + str(arr))
del arr[1]
print('del [1].. ' + str(arr))
poped = arr.pop(0)
print("pop (0).. " + str(arr))
arr.insert(0, "lee3")
print("insert (0).. " + str(arr))
arr.remove("wang5")
print('remove.. ' + str(arr))
arr.append("mzj")
print("append.. " + str(arr))
arr.sort(reverse=True)
print("永久排序.. " + str(arr))
print("临时排序.. " + str(sorted(arr)))
arr.reverse()
print("reverse.. " + str(arr))
print('遍历------------------------------------')
for times in arr:
    print(times)
print("不缩进就不在for中执行")
for i in range(1, 3):
    print(i)
digits = list(range(5, 101, 5))
print(digits)
print(min(digits), max(digits), sum(digits))
squares = [value ** 2 for value in range(1, 11)]
print(squares)
print(squares[1:3] + squares[:3] + squares[5:] + squares[-2:])
squares_copy = squares[:]
squares_copy2 = squares_copy
squares_copy.append(121)
print(squares_copy)
print(squares_copy2)
# 元组里的元素不能修改，但可以重新定义元组
dimentions = (800, 600)
print(dimentions)
dimentions = (1024, 768)
print(dimentions)
print('条件------------------------------------')
cars = ['audi', 'bmw', 'subaru', 'toyota']
# cars = []
if cars:
    for car in cars:
        if car == 'bmw' or car in ['BMW']:
            print(car.upper())
        elif car.lower() != 'toyota':
            print(car.title())
        else:
            print(car.lower())
else:
    print("cars is empty!")
print('字典------------------------------------')
dic1 = {'li4': 33, 'wang5': 44, 'ma6': '33'}
print(dic1)
dic1['li4'] = 44
del dic1['ma6']
print("li4=" + str(dic1['li4']) + ",wang5=" + str(dic1['wang5']))
for k, v in dic1.items():
    print('i ' + k + '=' + str(v))
for k in dic1.keys():
    print('k ' + k + '=' + str(dic1[k]))
for v in set(dic1.values()):
    print('v ' + str(v))
print('------------------------------------')
prompt = "Please Input: 'quit' to exit>>"
msg = ""
times = 1
while msg != 'quit':
    if msg == ':q' or times > 10:
        print("msg=" + msg + " x=" + str(times))
        break;
    msg = input(prompt)
    if msg != 'quit':
        print(msg)
    times += 1
print('------------------------------------')
# Python之禅
# import this
