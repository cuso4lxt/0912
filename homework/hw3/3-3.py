# 编写一个函数，使其能够用正则表达式的方式简单验证身份证号是否合法

# 导入了Python标准库中的re模块，该模块提供正则表达式相关的函数和方法
import re

def is_valid_id_number(id_number):
    pattern = r'(^\d{15}$)|(^\d{17}([0-9]|X)$)'
    # re.match()
    # 会尝试从字符串的开始位置匹配正则表达式 pattern，并返回一个匹配对象，如果没有找到匹配，则返回 None。
    return bool(re.match(pattern, id_number))

id = input()

if is_valid_id_number(id):
    print("This is a valid id number.")
else:
    print("This is not a valid number.")
