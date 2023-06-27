text = str(input("Введіть текст в якому бажаєте перевірити. "))
devided_text = text.split()

for word in devided_text:
    if word == word[::-1]:
        print(f"{word} слово являється паліндромом")
    else:
        print(f"{word} слово не являється паліндромом")
