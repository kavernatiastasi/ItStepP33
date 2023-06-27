tuple1 = (1, 2, 3, 4, 9, 6, 7, 8, 9)
tuple2 = (2, 2, 6, 8, 9, 12, 14, 16, 18)
tuple3 = (1, 3, 5, 7, 9, 11, 13, 15, 17)

elements = []

for tup1, tup2, tup3 in zip(tuple1, tuple2, tuple3):
    if tup1 == tup2 == tup3:
        elements.append(tup1)

print("Елементи, які є в кожному з кортежів і знаходяться в кожному з них на тій самій позиції:", elements)