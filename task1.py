number_one = float(input("Введіть перше число: "))
number_two = float(input("Введіть друге число: "))
number_three = float(input("Введіть третє число: "))
action = input("Введіть дію (+ або *):")
result = ""
if action == "+":
    result = number_one + number_two + number_three
elif action == "*":
    result = number_one * number_two * number_three
else:
    print("Нажаль така дія не підтримується")
print("Результат:", result)