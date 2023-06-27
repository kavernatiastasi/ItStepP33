while True:
    try:
        number = int(input("Введіть ціле число: "))
        break
    except ValueError:
        print("Введено не коректне значення!")

positiv = "Number is positive"
negativ = "Number is negative"
zero = "Number is equal zero"

if number > 0:
    print(positiv)
elif number < 0:
    print(negativ)
elif number == 0:
    print(zero)
else:
    raise ValueError("Введено не вірне значення!")
