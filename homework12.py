
month = {1: "Січень", 2: "Лютий", 3: "Березень", 4: "Квітень", 5: "Травень", 6: "Червень", 7: "Липень", 8: "Серпень",
9: "Вересень", 10: "Жовтень", 11: "Листопад", 12: "Грудень"}

while True:
    try:
        set_number = int(input("Введіть номер місяця року: "))
        if set_number not in month:
            raise ValueError("Введіть число не меньше 1 і не більше 12")
        break
    except ValueError as error:
        print(error)

print(month[set_number])
