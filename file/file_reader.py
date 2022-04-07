'''
# 读取整个文件(使用相对路径)
with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
'''

'''
# 读取整个文件(使用绝对路径)
file_path = '/Users/wangxuan/Python_wx/file/text_files/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
'''

'''
# 逐行读取文件
with open('text_files/pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())
'''

'''
# 在with代码块外使用open()返回的文件对象
# 创建变量存储文件中的精确到30位小数的圆周率的值
# 读取文本文件时，Python将其中的所有文本都解读为字符串
with open('text_files/pi_digits.txt') as file_object:
    # readlines()从文件中读取每一行，并将其存储在一个列表中
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
'''

'''
# 写入多行内容到空文件
fileName = 'programming.txt'
with open(fileName,'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
'''

'''
# 附加新内容到已存在文件
fileName = 'programming.txt'
with open(fileName,'a') as file_object:
    file_object.write("hhh.\n")
    file_object.write("ooo.\n")
'''






    