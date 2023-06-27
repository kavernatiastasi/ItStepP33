while True:
    try:
        number_one = input("Введіть перший номер: ")
        if not number_one.isdigit():
            raise ValueError("Введено недопустимий символ, введіть число!")
        number_two = input("Введіть другий номер: ")
        if not number_two.isdigit():
            raise ValueError("Введено недопустимий символ, введіть число!")
        number_three = input("Введіть третій номер: ")
        if not number_three.isdigit():
            raise ValueError("Введено недопустимий символ, введіть число!")
        together = number_one + number_two + number_three
        print("Утворене число: " + together)
        break
    except ValueError as error:
        print(error)


