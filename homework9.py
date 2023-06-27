text = str(input("Введіть текст: "))
words = str(input("Введіть список зарезервованих слів: ")).split(",")

for words_replaced in words:
    text = text.replace(words_replaced, words_replaced.upper())

print("Замінений текст:", text)