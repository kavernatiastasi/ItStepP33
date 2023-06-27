while True:
    try :
        number = int(input("Введіть номер дня тижня: "))
        if number > 7:
            raise ValueError("Число має бути не більше ніж 7")
        elif number < 1:
            raise ValueError("Число має бути не меньше ніж 1")
        break
    except ValueError as error:
        print(error)

if number == 1:
    print("Понеділок")
elif number == 2:
    print("Вівторок")
elif number == 3:
    print("Середа")
elif number == 4:
    print("Четвер")
elif number == 5:
    print("П'ятниця")
elif number == 6:
    print("Субота")
elif number == 7:
    print("Неділя")
