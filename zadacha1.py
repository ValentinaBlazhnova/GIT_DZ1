day = int(input('Введите цифру, обозначающую день недели = '))
if day >= 1 and day <=5:
    print(f'{day} -> нет')
elif 6 <= day <= 7:
    print(f'{day} -> да')
else:
    print('Такого дня недели не существует!')

