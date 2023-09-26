# 十到二进制小数的转换

def decimal_to_binary(num):
    # 整数部分的转换
    integer_part = int(num)
    binary_integer = ""
    while integer_part:
        # 字符串连接
        binary_integer = str(integer_part % 2) + binary_integer
        integer_part //= 2

    # 小数部分的转换
    decimal_part = num - int(num)
    binary_fraction = ""
    while decimal_part and len(binary_fraction) < 8:
        decimal_part *= 2
        binary_fraction += str(int(decimal_part))
        decimal_part -= int(decimal_part)

    return binary_integer + "." + binary_fraction

num = float(input())
print(decimal_to_binary(num))
