reverse = " "
while True:
    try:
        number = input("Введіть чотиризначне число: ")

        # перевернути число
        reverse = int(number[::-1])
        break
    except ValueError:
        print("Введено не вірне значення!")
print("Перевернуте число:", reverse)
