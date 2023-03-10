"=========================работа с файлами========================="
# open - функция, которая позволяет открывать файлы в определенном порядке
# r -read (только для чтения)
# w - write (тольок для перезаписи, каждый раз при открытии очищает файл)
# a - append (только дляь записи, добавляется в конец)
# x - создает файл, но если файл уже есть - ошибка
# b - бинарный вид

"===============================Read=============================="
file = open('test.txt')
#если твкого файл нет - выйдет ошибка
#если не указать режим - откроется в ржиме чтения


print(dir(file))

print("readable", file.readable()) # True
print("writable", file.writable()) # False

print(file.read()) #считает от начала до конца

file.seek(5) #перенос каретки в начало (на индекс 5)
print(file.read()) #'', пусто потому что коретка в конце файла

file.seek(0) #перенос каретки в начало (на индекс 0)
print(file.read(5)) # 'hello' считываем 5 символов
print(file.read()) # world beka считываем от 5 до конца

file.seek(0)
print(file.readline()) # 'hello\n' считывает до n
print(file.readline()) # 'world\n' считывает до n

file.seek(10)
print(file.tell()) #10 показывает место нахождение каретки

print(file.read())
print(file.tell()) #16

file.write

print(file.name) # 'test.txt'
print(file.closed) # False
file.close() # !важно закрывать файл
print(file.closed) # True

"=================================write=================================="
file = open("new_file.txt", 'w')
# если файл нет - создает
# если есть - очищает

print("readable", file.readable()) # False
print("writable", file.writable()) # True

# file.read()
# io.UnsupportedOperation: not readable
# !в режиме записи чтение запрещено

file.write('Hello ')
file.write('Makers')
# Hello Makers

file.writelines(['Hello', 'World'])
# Hello MakersHelloWorld

file.writelines(['\nNew\nLine'])
# Hello MakersHelloWorld
# New
# Line

file.seek(0)
file.write("AAA")
# AAAlo MakersHelloWorld
# New
# Line

file.close()






"====================================append================================="
file = open("new_file2.txt", 'a')
# если файла нет - создается новый

print("readable", file.readable()) # False
print("writable", file.writable()) # True

file.write('Hello')
# дозапись идет в конец файла (старые данные не удаляются)

file.seek(0)
file.write("New")
# все равно в конец дозапись

file.close()

"============================Контекстный менеджер======================"

# try:
#     file = open("aaa.txt", 'w')
#     file.read()
# finally:
#     file.close()


with open('test.txt') as f:
    f.read()
    f.seek(0)
    f.read()
    print(f.closed) # False
# файл закрывается   
print(f.closed) # True

with open("python.jpg", 'rb') as image:
    print(image.read())

with open("python.jpg", 'rb') as image:
    binary_image = image.read()

with open("new_image.jpg", 'wb') as file:
    file.write(binary_image)