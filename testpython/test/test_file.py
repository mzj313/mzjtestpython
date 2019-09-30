# -*- coding: GBK -*-
import json
import os

# with �Ὣ�ļ��ڲ���ʱ�Զ��ر�
try:
    with open('../pi_million_digits.txt') as file_pi:
        # 1.������
        # contents = file.read()
        # print(contents.rstrip())
        # 2.���ж�
        # for line in file:
        #     print(line.rstrip())
        # 3.���е��б�
        lines = file_pi.readlines()
        pi = ''
        for line in lines:
            pi += line.strip()
        print(pi[:30] + "..." + str(len(pi)))
except FileNotFoundError:
    print("File not found!")
else:
    birthday = '491001'
    print(birthday + " exists in ��: " + str(birthday in pi))
print("--------------------")
# д�ļ�
with open('../test.txt', 'w', encoding='UTF-8') as file_test:
    print(file_test.encoding)
    file_test.write("�����ļ�д��")
print("--------------------")
try:
    with open('../alice.txt') as f_alice:
        contents = f_alice.read()
except FileNotFoundError:
    pass
else:
    # �����ļ����°������ٸ�����
    words = contents.split()
    num_words = len(words)
    print("The file alice.txt has about " + str(num_words) + " words.")
print("--------------------")
numbers = [1, 3, 5, 7, 9, 11, 13]
filename = '../tmp.json'
with open(filename, 'w') as f_obj:
    print("��json���浽�ļ���..")
    json.dump(numbers, f_obj)
with open(filename) as f_obj:
    print("���ļ�����ȡjson..")
    numbers = json.load(f_obj)
    print(numbers)
os.remove(filename)
