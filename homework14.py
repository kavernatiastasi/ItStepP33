while True:
    try:
        number1 = int(input("Введіть перше число: "))
        break
    except ValueError:
        print("Введене значення не є числом, введіть число!")

while True:
    try:
        number2 = int(input("Введіть друге число: "))
        break
    except ValueError:
        print("Введене значення не є числом, введіть число!")
not_equal = "Числа не рівні"
if number1 == number2:
    print("Число", number1, "і число", number2, "рівні!")
elif number1 < number2:
    print(not_equal)
    print(number1, number2)
else:
    print(not_equal)
    print(number2, number1)
