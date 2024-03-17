def z1():
    a = int(input("Введите число: "))
    if a % 3 == 0:
        print(f"Число {a} делится на 3")
    else:
        print(f"Число {a} не делится на 3")

def z2():
 try:
     a = int(input("Введите число: "))
     res = 100 / a
     print(f"Результат деления 100 на {a} : {res}")
 except ValueError:
     print("Ошибка! Вы ввели не число")
 except ZeroDivisionError:
     print("Ошибка! Деление на ноль")

def z3():
    a = int(input("Введите день: "))
    b = int(input("Введите месяц: "))
    c = input("Введите год: ")

    d = int(c[-2:])
    if a * b == d:
        print("Дата магическая!")
    else:
        print("Дата НЕ магическая")

def z4():
    f = 0
    s = 0
    a = str(input("Введите номер билета: "))
    if len(a) % 2 == 0:
        half = len(a) // 2
        f_half = int(a[:half])
        s_half = int(a[half:])
        for i in range(half):
            f = int(f) + int(a[i])
        for i in range(half, len(a)):
            s = int(s) + int(a[i])
        if f == s:
            print(f"Билет {a} - счастливый")
        else:
            print(f"Билет {a} - несчастливый")
    else:
        print("Неверный номер")
z1()
z2()
z3()
z4()