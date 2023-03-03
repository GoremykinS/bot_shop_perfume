import telebot
from telebot import types
import logging

# логирование
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

# цена порфюма
price1_1, price1_2, price1_3 = 1, 2, 3
price2_1, price2_2, price2_3 = 10, 20, 30
price3_1, price3_2, price3_3 = 100, 200, 300

sum1_1, sum1_2, sum1_3,sum2_1, sum2_2, sum2_3, sum3_1, sum3_2, sum3_3 = 0,0,0,0,0,0,0,0,0
volume1, volume2, volume3 = 0,0,0
id_product = 0
n = 0
total_sum = 0

bot = telebot.TeleBot("6063112911:AAEI-eOtXPoLN6uxO1B_M_BviJwgHzHlauk")


@bot.message_handler(commands=['start'])
def start(message):
    # логирование
    logging.info('---------------')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-проводник в мире ароматов!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global sum1_1, sum1_2, sum1_3,sum2_1, sum2_2, sum2_3, sum3_1, sum3_2, sum3_3
    global id_product, total_sum
    global volume1, volume2, volume3

    if message.text == '👋 Поздороваться':
        sum1_1, sum1_2, sum1_3,sum2_1, sum2_2, sum2_3, sum3_1, sum3_2, sum3_3 = 0,0,0,0,0,0,0,0,0
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Отзывы')
        btn2 = types.KeyboardButton('Как со мной связаться')
        btn3 = types.KeyboardButton('Ассортимент')
        # btn4 = types.KeyboardButton(text="Контактный телефон", request_contact=True)
        #
        # @bot.message_handler(content_types=['contact'])
        # def contact(message):
        #     if message.contact is not None:
        #         logging.info(message.contact.phone_number)

        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup)




    elif message.text == 'Отзывы':
        bot.send_message(message.from_user.id, 'Перейдите по ссылке на сайт Авито. Все отзывы представлены там ' + '[ссылке](https://www.avito.ru/user/c638cc63c118c7f10ad7af4ec5ba5b78/profile?src=sharing)', parse_mode='Markdown')

    elif message.text == 'Как со мной связаться':
        bot.send_message(message.from_user.id, 'Контакты вы можете найти на сайте Авито ' + '[ссылке](https://www.avito.ru/user/c638cc63c118c7f10ad7af4ec5ba5b78/profile?src=sharing)', parse_mode='Markdown')

    if message.text == 'Ассортимент' or message.text == 'к списку ароматов':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4 = types.KeyboardButton('Amouage Sunshine')
        btn5 = types.KeyboardButton('M-A Barrois Ganymede')
        btn6 = types.KeyboardButton('Memo Kedu')
        markup.add(btn4, btn5, btn6)
        bot.send_message(message.from_user.id, 'Выберите интересующий Вас аромат', reply_markup=markup)

    def rez(*args):
        return sum(args)

    if message.text == 'Amouage Sunshine':
        id_product = 1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4 = types.KeyboardButton('2 ml')
        btn5 = types.KeyboardButton('5 ml')
        btn6 = types.KeyboardButton('10 ml')
        btn7 = types.KeyboardButton('передумал')
        btn8 = types.KeyboardButton('посчитать')
        btn9 = types.KeyboardButton('к списку ароматов')
        markup.add(btn4, btn5, btn6, btn7, btn8, btn9)
        bot.send_message(message.from_user.id, 'Выберите интересующий Вас объем', reply_markup=markup)


    if message.text == '2 ml' and id_product == 1:
        volume1 += 2
        sum1_1 += price1_1
        bot.send_message(message.from_user.id, '+ 2 ml за '+ str(price1_1) +' руб')

    if message.text == '5 ml' and id_product == 1:
        volume1 += 5
        sum1_2 += price1_2
        bot.send_message(message.from_user.id, '+ 5 ml за '+ str(price1_2) +' руб')

    if message.text == '10 ml' and id_product == 1:
        volume1 += 10
        sum1_3 += price1_3
        bot.send_message(message.from_user.id, '+ 10 ml за '+ str(price1_3) +' руб')


    if message.text == 'M-A Barrois Ganymede':
        id_product = 2
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4 = types.KeyboardButton('2 ml')
        btn5 = types.KeyboardButton('5 ml')
        btn6 = types.KeyboardButton('10 ml')
        btn7 = types.KeyboardButton('передумал')
        btn8 = types.KeyboardButton('посчитать')
        btn9 = types.KeyboardButton('к списку ароматов')
        markup.add(btn4, btn5, btn6, btn7, btn8, btn9)
        bot.send_message(message.from_user.id, 'Выберите интересующий Вас объем', reply_markup=markup)


    if message.text == '2 ml' and id_product == 2:
        volume2 += 2
        sum2_1 += price2_1
        bot.send_message(message.from_user.id, '+ 2 ml за '+ str(price2_1) +' руб')

    if message.text == '5 ml' and id_product == 2:
        volume2 += 5
        sum2_2 += price2_2
        bot.send_message(message.from_user.id, '+ 5 ml за '+ str(price2_2) +' руб')

    if message.text == '10 ml' and id_product == 2:
        volume2 += 10
        sum2_3 += price2_3
        bot.send_message(message.from_user.id, '+ 10 ml за '+ str(price2_3) +' руб')





    if message.text == 'Memo Kedu':
        id_product = 3
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4 = types.KeyboardButton('2 ml')
        btn5 = types.KeyboardButton('5 ml')
        btn6 = types.KeyboardButton('10 ml')
        btn7 = types.KeyboardButton('передумал')
        btn8 = types.KeyboardButton('посчитать')
        btn9 = types.KeyboardButton('к списку ароматов')
        markup.add(btn4, btn5, btn6, btn7, btn8, btn9)
        bot.send_message(message.from_user.id, 'Выберите интересующий Вас объем', reply_markup=markup)


    if message.text == '2 ml' and id_product == 3:
        volume3 += 2
        sum3_1 += price3_1
        bot.send_message(message.from_user.id, '+ 2 ml за '+ str(price3_1) +' руб')

    if message.text == '5 ml' and id_product == 3:
        volume3 += 5
        sum3_2 += price3_2
        bot.send_message(message.from_user.id, '+ 5 ml за '+ str(price3_2) +' руб')

    if message.text == '10 ml' and id_product == 3:
        volume3 += 10
        sum3_3 += price3_3
        bot.send_message(message.from_user.id, '+ 10 ml за '+ str(price3_3) +' руб')

    if message.text == 'передумал':
        sum1_1, sum1_2, sum1_3, sum2_1, sum2_2, sum2_3, sum3_1, sum3_2, sum3_3 = 0,0,0,0,0,0,0,0,0
        volume1, volume2, volume3 = 0, 0, 0
        bot.send_message(message.from_user.id, 'стоимость заказа = 0 руб', parse_mode='Markdown')

    if message.text == 'посчитать':
        total_sum = rez(sum1_1, sum1_2, sum1_3,sum2_1, sum2_2, sum2_3, sum3_1, sum3_2, sum3_3)
        bot.send_message(message.from_user.id, 'общая стоимость Вашего заказа = ' + str(total_sum) + ' руб', parse_mode='Markdown')
        if sum1_1 + sum1_2 + sum1_3 > 0:
            bot.send_message(message.from_user.id, 'объем Amouage Sunshine = ' + str(volume1) + ' ml стоимостью ' + str(sum1_1 + sum1_2 + sum1_3) + ' руб',
                         parse_mode='Markdown')
        if sum2_1 + sum2_2 + sum2_3 > 0:
            bot.send_message(message.from_user.id, 'объем M-A Barrois Ganymede = ' + str(volume2) + ' ml стоимостью ' + str(sum2_1 + sum2_2 + sum2_3) + ' руб',
                         parse_mode='Markdown')
        if sum3_1 + sum3_2 + sum3_3 > 0:
            bot.send_message(message.from_user.id, 'объем Memo Kedu = ' + str(volume3) + ' ml стоимостью ' + str(sum3_1 + sum3_2 + sum3_3) + ' руб',
                         parse_mode='Markdown')
        if sum1_1 + sum1_2 + sum1_3 > 0:
            logging.info('объем Amouage Sunshine = ' + str(volume1) + ' ml стоимостью ' + str(sum1_1 + sum1_2 + sum1_3) + ' руб')
        if sum2_1 + sum2_2 + sum2_3 > 0:
                logging.info('объем M-A Barrois Ganymede = ' + str(volume2) + ' ml стоимостью ' + str(sum2_1 + sum2_2 + sum2_3) + ' руб')
        if sum3_1 + sum3_2 + sum3_3 > 0:
                logging.info('объем Memo Kedu = ' + str(volume3) + ' ml стоимостью ' + str(sum3_1 + sum3_2 + sum3_3) + ' руб')



# логировать даные пользователя (телефон)
    if message.text == 'посчитать':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text="Оставить контактный телефон", request_contact=True)
        btn2 = types.KeyboardButton('к списку ароматов')
        @bot.message_handler(content_types=['contact'])
        def contact(message):
            if message.contact is not None:
                logging.info(message.contact.phone_number)
        markup.add(btn1,btn2 )
        bot.send_message(message.from_user.id, 'Заказ учтен! Оставьте контакный телефон (кнопка ниже) и '
                                               ' Мы с вами свяжемся', reply_markup=markup)







bot.polling(none_stop=True, interval=0)