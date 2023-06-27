print("Це програма для конвертування метри в такі величини як милі, дюйми та ярди.")
metre = float(input("Введіть кількість метрів:"))
print("Виберіть в яку величину конвертувати:\n1.\tМилі\n2.\tДюйми\n3.\tЯрди")
selecting = int(input("Ваш вибір: "))
mile = 0.000621371
inch = 39.3701
yard = 1.09361
result = ""
if selecting == 1:
    result = metre * mile
elif selecting == 2:
    result = metre * inch
elif selecting == 3:
    result = metre * yard
else:
    print("Невідома величина вимірювання")
print("Результат: ", result)
