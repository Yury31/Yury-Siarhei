try:
    x = int(input('Insert the number >> '))
except ValueError:
    print('Wrong value! Bye-bye!!')
    quit()
while True:
    print('If you wanna kB press #1')
    print('Or press #2 for bytes!')
    break
y = int(input('>> '))
if y == 1:
    print(x*1024, 'kB')
elif y == 2:
    print(x/1024, 'b')
else:
    print('ERROAARRR!!')


