import random

tuple1 = tuple(random.randint(1, 20) for i in range(10))
tuple2 = tuple(random.randint(1, 20) for i in range(10))
tuple3 = tuple(random.randint(1, 20) for i in range(10))
print(tuple1, tuple2, tuple3)

u_tuple1 = tuple(set(tuple1) - set(tuple2) - set(tuple3))
u_tuple2 = tuple(set(tuple2) - set(tuple1) - set(tuple3))
u_tuple3 = tuple(set(tuple3) - set(tuple1) - set(tuple2))

print("Унікальні елементи у кортежі 1:", u_tuple1)
print("Унікальні елементи у кортежі 2:", u_tuple2)
print("Унікальні елементи у кортежі 3:", u_tuple3)
