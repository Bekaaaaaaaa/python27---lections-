"====================типо функции==============="

#1) к изменяемым относится типом данных относится - set, списки, lists.
#2) к неизменяемым типом данным - кортежи(typles), intput, float, str
#3) что такое строки - неизменяемый, итерируемый, 
#4)
#5)
#6)ошибки - TabError, IndentationError, SyntaxError
# 1) Создайте словарь, где значениями будут являться числа. Найдите сумму этих значений.




'===============презентация==============='
print('С днем рождения тебя!')
print('Ты стал на год старше!')
print('С днем рождения тебя!')
print()

print('С днем рождения тебя!')
print('Ты стал на год старше!')
print('С днем рождения тебя!')
print()

print('С днем рождения тебя!')
print('Ты стал на год старше!')
print('С днем рождения тебя!')
print()

# это у нас без функции

def  С_днем_рождения():
    print('С днем рождения тебя!')
    print('Ты стал на год старше!')
    print('С днем рождения тебя!')
    print()
С_днем_рождения()
С_днем_рождения()
С_днем_рождения()


#теперь покажем что можно добавить в нашу функцию

def  С_днем_рождения(name, age):
    print(f'С днем рождения {name}!')
    print(f'Ты стал на {age} старше!')
    print('С днем рождения тебя!')
    print()
С_днем_рождения("родной", 20)
С_днем_рождения("любимая", 30)
С_днем_рождения("куратор", 25)


#так же можем посмотреть что будет если поменяем name and age

def  С_днем_рождения(age, name):
    print(f'С днем рождения {name}!')
    print(f'Ты стал на {age} старше!')
    print('С днем рождения тебя!')
    print()
С_днем_рождения("родной", 20)
С_днем_рождения("любимая", 30)
С_днем_рождения("куратор", 25)

#F - F-строки" обеспечивают краткий,
# читаемый способ включения значения выражений Python внутри строк.
# В исходном коде Python форматированная строка или по другому
# f-string - это буквальная строка с префиксом 'f' или 'F' ,
# которая содержит выражения внутри фигурных скобок {}. 
# Выражения заменяются их значениями.




1
2
3
