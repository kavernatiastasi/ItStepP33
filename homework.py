def print_my_text():
    just_text = "Don’t compare yourself with anyone in this world...\n" \
              "\tif you do so, you are insulting yourself.\n" \
              "Bill Gates"
    width = 40

    lines = just_text.split('\n')

    for line in lines:
        formatted_line = line.rjust(width)
        print(formatted_line)


def even_numbers(start, end):
    for number in range(start + 1, end):
        if number % 2 == 0:
            print(number)


def display_square(side_length, sign, filling):
    if filling:
        for i in range(side_length):
            print(sign * side_length)
    else:
        print(sign * side_length)
        for i in range(side_length - 2):
            print(sign + " " * (side_length - 2) + sign)
        print(sign * side_length)


def find_minimum(a, b, c, d, e):
    min_number = min(a, b, c, d, e)
    return min_number


def calculate_product(start, end):
    if start > end:
        start, end = end, start

    product = 1
    for number in range(start, end + 1):
        product *= number

    return product


def count_digits(number):
    count = len(str(number))
    return count


def is_palindrome(number):
    number_str = str(number)
    reversed_str = number_str[::-1]
    return number_str == reversed_str


while True:
    print("Оберіть функцію:")
    print("1. Вивести текст")
    print("2. Відобразити парні числа")
    print("3. Відобразити квадрат")
    print("4. Знайти мінімум")
    print("5. Обчислити добуток діапазону")
    print("6. Підрахувати кількість цифр у числі")
    print("7. Перевірити на паліндром")
    print("8. Вийти")

    choice = input("Ваш вибір (1-8): ")

    if choice == '1':
        print_my_text()
    elif choice == '2':
        start_number = int(input("Введіть початкове число: "))
        end_number = int(input("Введіть кінцеве число: "))
        even_numbers(start_number, end_number)
    elif choice == '3':
        length = int(input("Введіть довжину сторони квадрата: "))
        symbol = input("Введіть символ для відображення: ")
        is_filled = input("Заповнений квадрат? (True/False): ").lower() == "true"
        display_square(length, symbol, is_filled)
    elif choice == '4':
        num1 = int(input("Введіть перше число: "))
        num2 = int(input("Введіть друге число: "))
        num3 = int(input("Введіть третє число: "))
        num4 = int(input("Введіть четверте число: "))
        num5 = int(input("Введіть п'яте число: "))
        minimum = find_minimum(num1, num2, num3, num4, num5)
        print("Мінімальне число:", minimum)
    elif choice == '5':
        lower_number = int(input("Введіть нижню межу діапазону: "))
        upper_number = int(input("Введіть верхню межу діапазону: "))
        result = calculate_product(lower_number, upper_number)
        print("Добуток чисел у діапазоні:", result)
    elif choice == '6':
        num = int(input("Введіть число: "))
        digit_count = count_digits(num)
        print("Кількість цифр у числі:", digit_count)
    elif choice == '7':
        num = int(input("Введіть число: "))
        is_pal = is_palindrome(num)
        if is_pal:
            print("Число є паліндромом")
        else:
            print("Число не є паліндромом")
    elif choice == '8':
        print("До побачення!")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
