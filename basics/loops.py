'========================Циклы==========================='
#циклы - блок кода, который отрабатывается несколько раз
#for - цикл, который работает с итерируемыми оюьектами,
# цикл заканчивает свою работу, когда он доходит 
# до последнего элемента в интерируемом обьекте

#while - цикл который работает до тех пор пока условие верно 

list1 = ['hello', 10, True, [1,2,3]]
for element in list1:
    print(element)

string1 = 'hello world'
for letter in string1:
    print(letter)


i = 1
while i != 10:
    print('hello')
    i = i + 1

i = 0
while i:  #вообще не отработает потоу что False
    print('bekashreks')
    i = i + 1

'===========================ключевые слова====================='
# break - полностью останавливает цикл
# continue - переход к следующей итерации 

for i in range(10): 
    if i == 3:
        break #останавливает
    print(i) 
# 0
# 1
# 3

for i in range(10): 
    if i == 3:
        continue  # сразу идет за след числом после 3
    print(i) 
# 0 1 2 4 5 6 7 8 9

list1 - [1,2,3,4,5,6,1,1]
while 1 in list1:
    list1.remove(1)
print(list1)


#for придуман для итерируемых обьектов (list, dict, set, 