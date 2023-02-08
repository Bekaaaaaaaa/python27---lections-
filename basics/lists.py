'=================================lists==========================='
#список - это изменяемый, интерируемый, индексируемый и упорядочный тип данных, 
#предназначенный для хранения элементов с строгом породке.

list1 = [1, 3.5 'hello',(1, 2), None, True, False]
list1[0] # 10
list1[3] # [1, 2, 3]
list1[3][-1]  # нам выдало тройку из списка[1, 2, 3]
list1[-1] #False

list2 = list('hello')
print(list2) # ['h','e','l','l','o']

list3 = list(range(3,10,2))
print(list(range(3,5,7,9)))

print(list(range(5))) #[0,1,2,3,4]

'=========================изменяемость========================'
string = 'htllo'
res = string.upper()
print(string) #'hello'
print(res) # 'HELLO'

list1 = []
list1.append(1)
list1.append(2)
list1.append(3)
print(list1) #[1,2,3]

'================================ Методы списков ========================================'
# append - метод который добавляет элемент в конце списка
list1 = []
list1.append('hello')
list1.append(500)
list1.append([1, 2, 3])
print(list1) # ['hello', 500, [1,2,3]]

#remove - метод, который удалаяет елемент из списка по значанию
list2 = ['hello' 500, [1,2,3]]
list2.remove('hello') 
print(list2)  # [500, [1,2,3]]

# pop - метод, который удаляет элемент из списка по индексу, если этого индекса нет, выдаст
  # indexError

list3 = [10, 20, 30, 40, 50]
list3.pop()  # удаление списка с конца 
print(list3) #[10, 20, 30, 40,]
list3.pop(1) #удаление по индексу (1)
print(list3) #[10, 30, 40]

#также метод pop возвращяет удаленный элемент 
list4 = [10, 20, 30, 40]


# insert - метод, который добавляет элемент в список по индексу
list5 = [1,2,3,4]
list5.insert(0, 'hello')
print(list5) # ['hello', 1,2,3,4]


'=================задача=================='
#создайте список из чисел 
#расставьте список наоборот


# list = [1,2,3,4] 
# print(list[::-1]) #переворочивает список - [4,3,2,1]


# list = list(range(1,6)) #list = [1,2,3,4,5]
# list.reverse() #переворачивает список - [5.4.3.2.1]

#clear - чистит список полностью 
list1 = [1,2,3,4]
list1.clear()
print(list1) # [] - очистил 


#count - считает коль-во элемента, который передаем 

#index - возвращает индекс данного элемента
list2 = ['hello' 'world' 'makers']

#sort - сортирует число по велечине 
list3 = [31, 12, 11, 23]
list3.sort()
print(list3) # [11, 12, 23, 31]


#copy - возвращает копью списка

#extend - расширяет список другим списком