value=int(input("Enter your value to convert:"))
def decimal_to_convertor(value):
    return f'The decimal value of {value} in binary {bin(value)}, in octal {oct(value)} and  in hexadecimal {hex(value)}'
print(decimal_to_convertor (value))