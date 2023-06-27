import random

list_numbers = [random.randint(-100, 100) for i in range(10)]

print("Список чисел:", list_numbers)

negative_sum = 0
for num in list_numbers:
    if num < 0:
        negative_sum += num
print("Сума від'ємних чисел:", negative_sum)

even_plus = 0
for num in list_numbers:
    if num % 2 == 0:
        even_plus += num
print("Сума парних чисел:", even_plus)

odd_plus = 0
for num in list_numbers:
    if num % 2 != 0:
        odd_plus += num
print("Сума непарних чисел:", odd_plus)

multiple = 1
for i in range(len(list_numbers)):
    if i % 3 == 0:
        multiple *= list_numbers[i]
print("Добуток елементів з індексами, кратними 3:", multiple)

min_num = min(list_numbers)
max_num = max(list_numbers)
between = 1
for num in list_numbers[list_numbers.index(min_num):list_numbers.index(max_num) + 1]:
    between *= num
print("Добуток елементів між мінімальним та максимальним елементом:", between)

positive_numbers = []
for num in list_numbers:
    if num > 0:
        positive_numbers.append(num)
    if len(positive_numbers) == 2:
        break
if len(positive_numbers) != 2:
    print("У списку менше двох додатніх елементів.")
else:
    start_index = list_numbers.index(positive_numbers[0])
    end_index = list_numbers.index(positive_numbers[1])
    if start_index > end_index:
        start_index, end_index = end_index, start_index
    sumbetween = sum(list_numbers[start_index + 1:end_index])
print("Сума елементів, що знаходяться між першим та останнім додатним елементом:", sumbetween)
