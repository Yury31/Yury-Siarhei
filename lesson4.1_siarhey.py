try:
    a = int(input('Введите число 1 > '))
    b = int(input('Введите число 2 > '))
except ValueError:
    print('Ошибочка, вводите цифры а не букыв! ')
else:
    try:
        q = (a % b)
        q1 = (a/b)
        q2 = (a//b)
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
    else:
        if a > b:
            if q == 0:
                print('Число ', a, 'делится на число ', b, '.'
                      'Частное равно', q1, '.')
            elif q >= 1:
                print('Число ', a, 'делится на число ', b, '.'
                      'Частное равно', q2, '. Остаток равен ', q, '.')
        elif a < b:
            print('Число ', a, 'не делится на число ', b, '.')


