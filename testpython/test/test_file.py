# -*- coding: GBK -*-
import json
import os

# with 会将文件在不用时自动关闭
try:
    with open('../pi_million_digits.txt') as file_pi:
        # 1.读内容
        # contents = file.read()
        # print(contents.rstrip())
        # 2.逐行读
        # for line in file:
        #     print(line.rstrip())
        # 3.读行到列表
        lines = file_pi.readlines()
        pi = ''
        for line in lines:
            pi += line.strip()
        print(pi[:30] + "..." + str(len(pi)))
except FileNotFoundError:
    print("File not found!")
else:
    birthday = '491001'
    print(birthday + " exists in π: " + str(birthday in pi))
print("--------------------")
# 写文件
with open('../test.txt', 'w', encoding='UTF-8') as file_test:
    print(file_test.encoding)
    file_test.write("测试文件写入")
print("--------------------")
try:
    with open('../alice.txt') as f_alice:
        contents = f_alice.read()
except FileNotFoundError:
    pass
else:
    # 计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("The file alice.txt has about " + str(num_words) + " words.")
print("--------------------")
numbers = [1, 3, 5, 7, 9, 11, 13]
filename = '../tmp.json'
with open(filename, 'w') as f_obj:
    print("将json保存到文件中..")
    json.dump(numbers, f_obj)
with open(filename) as f_obj:
    print("从文件中提取json..")
    numbers = json.load(f_obj)
    print(numbers)
os.remove(filename)
