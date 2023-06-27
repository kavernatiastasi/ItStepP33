number_one = float(input("Введіть перше число: "))
number_two = float(input("Введіть друге число: "))
number_three = float(input("Введіть третє число: "))

print("Виберіть операцію:")
print("1 - знайти максимум")
print("2 - знайти мінімум")
print("3 - знайти середнє арифметичне")

selection = int(input("Ваш вибір: "))

if selection == 1:
    print("Максимум: ", max(number_one, number_two, number_three))
elif selection == 2:
    print("Мінімум: ", min(number_one, number_two, number_three))
elif selection == 3:
    average = (number_one + number_two + number_three) / 3
    print("Середнє арифметичне: ", average)
else:
    print("Неправильний вибір операції")
