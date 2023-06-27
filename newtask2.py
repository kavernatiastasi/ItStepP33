import random

list_numbers = []
for i in range(10):
    list_numbers.append(random.randint(-10, 10))
print("Список випадкових чисел: ", list_numbers)
positiveNum = []
negativeNum = []
evenNum = []
oddNum = []

for num in list_numbers:
    if num > 0:
        positiveNum.append(num)
    elif num < 0:
        negativeNum.append(num)
    if num % 2 == 0:
        evenNum.append(num)
    else:
        oddNum.append(num)

print("Парні числа: ", evenNum)
print("Непарні числа: ", oddNum)
print("Від'ємні числа: ", negativeNum)
print("Додатні числа: ", positiveNum)