while True:
    try:
        main_side = float(input("Введіть основу трикутника: "))
        height = float(input("Введіть висоту трикутника: "))
        square = main_side * height / 2
        break
    except ValueError:
        print("Введено не вірне значення, переконайтесь, що вводите вірне значення!")

print("Площа трикутника дорівнює = ", square)