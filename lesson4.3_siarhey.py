_list = []
try:
    while True:
        number = (input('> '))
        if not number:
            break
        number = int(number)
        _list.append(number)
except ValueError:
    print('Ошибочка, вводите целое число ! ')
    quit()
x = sum(_list)
y = len(_list)
z = (x/y)
result = []
for i in _list:
    if z > i:
        result.append(i)
print(result)

