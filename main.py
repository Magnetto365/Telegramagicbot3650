from settings import bot


@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id, "Для активування магічного бота напишіть /continue")


@bot.message_handler(commands=['continue'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Доброго дня, це MagicBot - бот, який вміє показувати фокуси.")
    bot.send_message(message.chat.id, "Для того, щоб подивитись фокус, напишіть /х, де х - номер від 1 до 5(номер фокусу)")
    bot.send_message(message.chat.id, "Ось весь список: /1 - перший фокус, /2 - другий фокус,"
                                      " /3 - третій фокус, /4 - четвертий фокус, /5 - п'ятий фокус.")



def mystery1answer(message):
    bot.send_message(message.chat.id, "Це 4, чи не так?)")


def mystery2answer(message):
    k = message.text
    k1 = int(k) - 250
    k2 = k1/100
    # k3 = k1-k2
    # k4 = f"{k2}.{k3}"
    bot.send_message(message.chat.id, f"Це {k2}, чи не так?)")

def mystery3answer(message):
    k = message.text
    kt = int(k) - 865
    k1 = kt // 100
    k2 = kt - k1*100
    t = ""
    if k1 <= 10:
        t = "0"
    bot.send_message(message.chat.id, f"Це ваша дата: {k2}.{t}{k1}?)")


def mystery4answer(message):
    k = message.text
    k1 = int(k) - 35
    bot.send_message(message.chat.id, f"Це {k1}, чи не так?)")


def mystery5answer(message):
    k = message.text
    k1 = int(k) // 100
    k2 = int(k) - k1*100
    bot.send_message(message.chat.id, f"Вам {k2} років)")


@bot.message_handler(commands=['1'])
def mystery1(message):
    bot.send_message(message.chat.id, "Загадайте натуральне число. Помножте на 2.")
    bot.send_message(message.chat.id, "Додайте 8. Поділіть на 2")
    msg = bot.send_message(message.chat.id, "Відніміть своє перше число. Напишіть щось у чат коли будете готові.")
    bot.register_next_step_handler(msg, mystery1answer)


@bot.message_handler(commands=['2'])
def mystery2(message):
    bot.send_message(message.chat.id, "Згадайте дату свого дня народження. Візміть з неї тільки число(без місяця) і помножте на 2.")
    bot.send_message(message.chat.id, "Додайте 5. Помножте на 50")
    msg = bot.send_message(message.chat.id, "Додайте місяць свого народження(грудень - 12, березень - 3). Напишіть число, що вийшло у чат.")
    bot.register_next_step_handler(msg, mystery2answer)


@bot.message_handler(commands=['3'])
def mystery3(message):
    bot.send_message(message.chat.id, "Згадайте якусь важливу дату. Тепер помножте номер місяця на 5 (грудень - 12, березень - 3), додати 6.")
    bot.send_message(message.chat.id, "Помножте на 4, додайте 9, помножте на 5.")
    msg = bot.send_message(message.chat.id, "Додайте 700 і число(без місяця) цієї дати(24 червня - 24).Напишіть число, що вийшло у чат.")
    bot.register_next_step_handler(msg, mystery3answer)


@bot.message_handler(commands=['4'])
def mystery4(message):
    bot.send_message(message.chat.id, "Загадайте якесь натуральне двухзначне число. Помножте його цифру десятків на 2,"
                                      " додайте 5, а те, що вийшло, помножте на 5.")
    msg = bot.send_message(message.chat.id, "Додайте 10 і цифру одиниць з початкового двухзначного числа."
                                            " Напишіть число, що вийшло у чат.")
    bot.register_next_step_handler(msg, mystery4answer)


@bot.message_handler(commands=['5'])
def mystery5(message):
    bot.send_message(message.chat.id, "Згадайте розмір своєї ноги. Помножте його на 100.")
    bot.send_message(message.chat.id, "Відніміть свій рік народження.")
    msg = bot.send_message(message.chat.id, "Додайте сьогоднішній рік. Напишіть число, що вийшло у чат.")
    bot.register_next_step_handler(msg, mystery5answer)

bot.infinity_polling()