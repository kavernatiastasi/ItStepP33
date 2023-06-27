import telebot
import datetime
import locale
token = "6039077135:AAEVY0I5SUFj4rTkKwedMokGCBBeK8VnqXI"
bot = telebot.TeleBot(token)
locale.setlocale(locale.LC_ALL, "uk_UA.UTF-8")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привіт! Я Python помічник. Я готовий допомогти тобі з Python! Щоб дізнатись про"
                                      " мої можливості введіть команду /help")


@bot.message_handler(commands=['help'])
def help_function(message):
    text = "Ось кілька команд, які я розумію:\n"
    text += "/start - Розпочати спілкування\n"
    text += "/python - Загальна інформація про цю мову\n"
    text += "/info - Описання помічника та його функцій\n"
    text += "/bool - Інформація про тип данних boolean\n"
    text += "/dict - Інформація про словники\n"
    text += "/float - Інформація про тип данних float\n"
    text += "/int - Інформація про числовий тип данних  int\n"
    text += "/str - Інформація про рядковий тип данних\n"
    text += "/tuple - Інформація про кортежі\n"
    text += "/range - Інформація про тип данних range\n"
    text += "/set - Інформація про тип данних set\n"
    text += "/list - Інформація про списки\n"
    text += "/nowday - Отримати сьогоднішній день\n"
    text += "/nowdate - Отримати поточну дату\n"
    text += "/nowtime - Отримати поточний час\n"
    text += "/nowweek - Отримати номер поточного тижня"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['python'])
def python_info(message):
    text = "Python - це мова програмування, яка відома своєю простотою та читабельністю коду. " \
           "Вона широко використовується для веб-розробки, наукових обчислень, штучного інтелекту та багатьох інших " \
           "сфер."
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['info'])
def info_bot(message):
    text = "Цей бот може вам допомогти розібратись з деякими аспектами цієї програмної мови.  "
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['bool'])
def bool_type(message):
    text = "Bool це незмінний логічний тип данних. \nПриклад: True або False.  "
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['dict'])
def dict_type(message):
    text = "dict - змінюваний тип данних. Словник (асоціативний масив), є колекцією пар «ключ-значення»; значення " \
           "може бути будь-якого типу, ключ повинен мати тип, що хешується. Словники записуються в {} дужках. " \
           "\nНаприклад: {'key1': 1.0, 3: False}"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['float'])
def float_type(message):
    text = "float - незмінний тип данних. Число з плаваючою комою. Ступінь точності залежить від платформи, але " \
           "на практиці зазвичай реалізується у вигляді 64-бітного 53-розрядного числа. \nПриклад вигляду числа " \
           "типу float --> 1.414"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['int'])
def int_type(message):
    text = "int - незмінний тип данних. Це ціле число необмеженного розміру. \nПриклад числа --> 42"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['str'])
def str_type(message):
    text = "str - незмінний тип данних. Це рядковий тип данних. \nНаприклад: \"Python\" або \'Python'"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['tuple'])
def tuple_type(message):
    text = "tuple - незмінний тип данних. Це кортеж. Може містити в собі різні типи даних. Може використовуватися" \
           " як незмінний список і як записи з не іменованими полями. \nНаприклад: (4.0, 'string', True)"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['range'])
def range_type(message):
    text = "range - незмінний тип данних. Послідовність цілих чисел від одного значення до іншого, зазвичай " \
           "використовується для повторення операції кілька разів за допомогою for. \nНаприклад: range(1, 10) або " \
           "range(10, -5, -2)"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['set'])
def set_type(message):
    text = "set - змінюваний тип данних. Неупорядкована множина, котра не містить дублікатів; може містити " \
           "в собі різні типи даних, що хешуються. \nНаприклад: set() а також {4.0, 'string', True}"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['list'])
def list_type(message):
    text = "list - змінюваний тип данних. Це список який може містити в собі різні типи даних. \nНаприклад: " \
           "[4.0, 'string', True]"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['nowday'])
def list_type(message):
    current_date = datetime.date.today()
    day_of_week = current_date.strftime("%A")
    bot.send_message(message.chat.id,  text="Сьогодні: " + day_of_week)


@bot.message_handler(commands=['nowdate'])
def list_type(message):
    current_date = datetime.date.today()
    formatted_date = current_date.strftime("%d-%m-%Y")
    bot.send_message(message.chat.id,  text="Сьогодні: " + formatted_date)


@bot.message_handler(commands=['nowtime'])
def list_type(message):
    current_time = datetime.datetime.now().time()
    formatted_time = current_time.strftime("%H:%M:%S")
    bot.send_message(message.chat.id,  text="На даний момент:  " + formatted_time)


@bot.message_handler(commands=['nowweek'])
def list_type(message):
    current_date = datetime.date.today()
    year, week_number, _ = current_date.isocalendar()
    bot.send_message(message.chat.id, text="Сьогодні: Тиждень " + str(week_number) + " року " + str(year))


@bot.message_handler(content_types=["text"])
def get_user_text(message):
    if message.text == "hello":
        bot.send_message(message.chat.id, "І тобі привіт")
    elif message.text == "python":
        bot.send_message(message.chat.id, "O, ти вивчаєш пайтон? Kруто!!!")
    elif message.text == "python logo":
        photo = open("123.png", 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "datetime documentation":
        doc = open("datetime_documentation.html",  "r", encoding="utf-8")
        bot.send_document(message.chat.id, doc, caption="Ось документація по модулю datetime. Звертайтесь!")
    elif message.text == "logging documentation":
        doc = open("logging_documentation.html",  "r", encoding="utf-8")
        bot.send_document(message.chat.id, doc, caption="Ось документація по модулю logging. Звертайтесь!")
    elif message.text == "os documentation":
        doc = open("os_module.html",  "r", encoding="utf-8")
        bot.send_document(message.chat.id, doc, caption="Ось документація по модулю os. Звертайтесь!")
    elif message.text == "re documentation":
        doc = open("re_documentation.html",  "r", encoding="utf-8")
        bot.send_document(message.chat.id, doc, caption="Ось документація по модулю re. Звертайтесь!")
    elif message.text == "sys documentation":
        doc = open("sys_documentation.html",  "r", encoding="utf-8")
        bot.send_document(message.chat.id, doc, caption="Ось документація по модулю sys. Звертайтесь!")
    elif message.text == "tkinter documentation":
        doc = open("tkinter_documentation.html",  "r", encoding="utf-8")
        bot.send_document(message.chat.id, doc, caption="Ось документація по модулю tkinter. Звертайтесь!")
    else:
        bot.send_message(message.chat.id, "я тебе не розумію")


bot.polling(none_stop=True)
