while True:
    try:
        metres = float(input("Введіть кількість метрів: "))
        break
    except ValueError:
        print("Не вірне значення")
while True:
    try:
        print("Введіть величину в яку конвертувати:\n1.\tСантиметри\n2.\tДециметри\n3.\tМіліметри\n4.\tМилі")
        choise = int(input("Ваш вибір: "))
        break
    except ValueError:
        print("Не вірне значення")
sm = 100
dec = 10
mm = 1000
miles = 0.000621371
result = 0
if choise == 1:
    result = metres * sm
elif choise == 2:
    result = metres * dec
elif choise == 3:
    result = metres * mm
elif choise == 4:
    result = metres * miles
else:
    print("Не вірне значення")

print("Ваш результат", result)