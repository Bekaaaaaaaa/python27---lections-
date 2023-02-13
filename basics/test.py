# x = 100
# y = 2
# if x%y==0:
#     print('x делится на y')
#     print(f"Частное {x//y}")
# else:
#     print("x не делится на y")
#     print(f"Частное: {x//y}")
#     print(f"Остаток: {x%y}")



# dict = {'a':1, 'b':2, 'a':3}
# list1 = [1,2,3]
# list2 = ['a', 'b', 'c']
# dict3 = dict(zip(list1, list2))
# print(dict3)

# dict = {'a':1, 'b':2, 'a':3}
# res = dict(zip(dict1.value(), dicts.keys()))
# print(res)



# dict1 = {
#     "a": {"key":1},
#     "b": {"key":2},
#     "c": {"key":3}
# }
# # res = {"a":1, "b":2, "c":3}
# res = {}
# for key, value in dict1.items():
#     res[key] = value['key']
# print(res)

lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
if len(lists) > 1:
    print(f'max_list {max(lists, key=len)}')
elif len(lists) < 1:
    print(f'min_list {min(lists, key=len)}')
else:
    print(False)



#задача на comprehension
list1 = [i for i in range(1,11) if i % 2 == 0]
print(list1)
#[2, 4, 6, 8, 10]


# #умножить на 100
list1 = range(1,11)
res = [i * 100 for i in range(1,11)]
print(res)

#распечать 5 раз 'hello'
res = ['hello' for i in range (5)]
print(res)
#['hello', 'hello', 'hello', 'hello', 'hello']

#соеденить users и hello 
users = ['test1', 'test1', 'test3']
res = ['Hello '+name for name in users]
print(res)
#['Hello test1', 'Hello test1', 'Hello test3']

res = [[x for x in range(1,i+1)]for i in range(1,6)]
print(res)

list1 = [[1,2,3],[4,5,6],[7,8,9]]
res = [1,2,3,4,5,6,7,8,9]
res = [i for inner_list in list1 for i in inner_list]
# res = []
# for inner_list in list1:
#     for i in inner_list:
#         res.append(i)
print(res)


#[1,2,3,4]
#['не четное','четное','не четное','четное']
res = ['четное' if i % 2 == 0 else 'не четное' for i in range(1,7)]
print(res)
#['не четное', 'четное', 'не четное', 'четное', 'не четное', 'четное']

#[[1],[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5]]
res = [[x for x in range(1, i+1)] for i in range(1,6)]
print(res)


#{1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 5]}
res = {i:[x for x in range(1, i+1)] for i in range(1,6)}
print(res)