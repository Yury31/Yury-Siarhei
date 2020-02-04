_list = []
while True:
    number = (input('> '))
    if not number:
        break
    try:
        number = int(number)
        _list.append(number)
    except ValueError:
        print('Вводите только целые вещественные числа!')
        quit(print('Попробуйте заново!'))
x = max(_list)
result = []
for i in _list:
    if abs(i) > x:
        result.append(i)
print(len(result), 'из элементов списка больше по модулю максимального числа.')

