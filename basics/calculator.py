"==================================калькулятор====================================="
# print('Для завершения 0 в качестве знака операции')


# while True:
#     s = input("знак(+,-,*,/): ")
#     if s == '0':
#         break
# if s not in ('+', '-', '*', '/'):
#     continue 
# a = float(input('a = '))
# b = float(input)

# if s == '+':
#     print(a + b)
# elif s == '-':
#     print(a - b)
# elif s == '*':
#     print(a * b)
# elif s == '/':
#     if b != 0:
#      print(a / b)
# else:
#     print('Деление на ноль!!')
# try:


while True:
    print('введите exit для выхода')
    s = input("знак(+,-,*,/,'**','//','%'): ")
    if s == 'exit':
        break
    a = float(input())
    b = float(input())
    if s == '+':
        print(a + b)
    elif s == '-':
        print(a - b)
    elif s == '*':
        print(a * b)
    elif s == '/':
        if b != 0:
            print(a / b)
        else:
            print('Нельзя делить на ноль дурачок')
    elif s == '%':
        if b != 0:
            print(a % b)
        else:
            print('Нельзя делить на ноль дурачок ')
    elif s == '//':
        if b != 0:
            print(a // b)
        else:
            print('Нельзя делить на ноль дурачок')
    elif s == '**':
        print(a ** b)
    else:
        print('Деление на ноль!!')


# num1 = float(input())
# num2 = float(input())


# print(num1/num2)
# try:
#     print(num1/num2)
# except ZeroDivisionError:
#     print('no')
# else:
#     print(num1/num2)

# print('Ya prodoljau rabotat')