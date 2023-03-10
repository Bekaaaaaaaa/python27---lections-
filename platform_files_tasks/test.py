"1"
import json
# with open('task1.json', 'r') as f:
#     python_obj = json.loads(f.read())
# with open('task1.py', 'w') as f:
#     f.write(str(python_obj))

"2"
# import json
# with open('task2.json', 'r') as f:
#     json_obj = f.read()
#     python_obj = json.loads(json_obj)
#     print(python_obj)

"3"
# import json

# python_obj = None
# # json.dumps(python_obj)
# json_obj = json.dumps(python_obj)
# print(json_obj)

"4"
# import json

# json_obj = "null" 
# # json.dumps(python_obj)
# python_obj = json.loads(json_obj)
# print(python_obj)

"5"
import json
users = [
    {
        'name': 'John',
        'last_name': 'Snow',
        'age': 26,
        'has_car': True,
    },
    {
        'name': 'Sam',
        'last_name': 'Bolt',
        'age': 4,
        'has_car': False,
    }
]


json_users = json.dumps(users)
print(json_users)