import random

tuple1 = tuple(random.randint(1, 20) for i in range(10))
tuple2 = tuple(random.randint(1, 20) for i in range(10))
tuple3 = tuple(random.randint(1, 20) for i in range(10))
print(tuple1, tuple2, tuple3)

elements = []

for elem in tuple1:
    if elem in tuple2 and elem in tuple3:
        elements.append(elem)

print("Спільні елементи в кортежах", elements)