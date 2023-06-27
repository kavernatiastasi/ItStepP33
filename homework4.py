num = input("Введіть число, що складається з чотирьох цифр: ")

# перетворимо рядок на список цифр і обчислимо добуток
product = 1
try:
    for digit in num:
        product *= int(digit)
except ValueError:
    print("Введіть число!")

print("Добуток цифр:", product)
