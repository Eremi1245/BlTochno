from copy import deepcopy

from telebot import TeleBot, types

from BlTochno.DataBase.models import Event, Category
from BlTochno.Telegram.commands import add_to_data, get_object
from secret import TOKEN

bot = TeleBot(TOKEN)
tg_commands=[
    '/my_day',
    '/my_week',
    '/add_event',
    '/add_category'
]
keyboard_response=''


@bot.message_handler(commands=['start'])
def bot_start(message):
        all_commands='\n'.join(tg_commands)
        bot.send_message(message.from_user.id, all_commands)

@bot.message_handler(commands=['my_day'])
def get_my_day(message):
    bot.send_message(message.from_user.id, 'Расписание на день')

@bot.message_handler(commands=['my_week'])
def get_my_week(message):
    bot.send_message(message.from_user.id, 'Расписание на неделю')

@bot.callback_query_handler(func=lambda message: True)
@bot.message_handler(commands=['add_event'])
def add_event(message,args:dict=None):
    if not args:
        args={'new_event':Event(),'attribute':''}
    new_event=args['new_event']
    attrib = args['attribute']
    if attrib and message.text!='/add_event':
        setattr(new_event, attrib, message.text)

    if not new_event.name:
        args.update({'attribute':'name'})
        bot.send_message(message.from_user.id, 'Введите название евента')
        bot.register_next_step_handler(message,add_event,args)
    elif not new_event.dt:
        args.update({'attribute':'dt'})
        bot.send_message(message.from_user.id, 'Введите Дату ивента')
        bot.register_next_step_handler(message,add_event,args)
    elif not new_event.tm:
        args.update({'attribute':'tm'})
        bot.send_message(message.from_user.id, 'Введите Время ивента')
        bot.register_next_step_handler(message,add_event,args)
    elif not new_event.category:
        args.update({'attribute':'category'})
        categories=get_object(Category)
        categories='\n'.join([f'{cat.name}' for cat in categories])
        question = 'Выбери id категории ивента\n'+categories
        bot.send_message(message.from_user.id, question)
        bot.register_next_step_handler(message,add_event,args)
    elif not new_event.desc:
        args.update({'attribute':'desc'})
        bot.send_message(message.from_user.id, 'Введите описание ивента\nВведите "нет" если описание не требуется')
        bot.register_next_step_handler(message,add_event,args)
    else:
        result=add_to_data(new_event)
        if result["status"]:
            bot.send_message(message.from_user.id, 'Евент добавлен')
        else:
            bot.send_message(message.from_user.id, f'Ошибка: {result["error"]}')

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    add_event(call["message"], call["args"])

@bot.message_handler(commands=['add_category'])
def add_category(message,args:dict=None):
    if not args:
        args={'new_category':Category(),'attribute':''}
    new_object=args['new_category']
    attrib = args['attribute']
    if attrib and message.text!='/add_category':
        setattr(new_object, attrib, message.text)

    if not new_object.name:
        args.update({'attribute':'name'})
        bot.send_message(message.from_user.id, 'Введите название категории')
        bot.register_next_step_handler(message,add_category,args)
    else:
        result=add_to_data(new_object)
        if result["status"]:
            bot.send_message(message.from_user.id, 'Категория добавлена')
        else:
            bot.send_message(message.from_user.id, f'Ошибка: {result["error"]}')


def get_name(message): #получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id,'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):

        keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes'); #кнопка «Да»
        keyboard.add(key_yes); #добавляем кнопку в клавиатуру
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='no');
        keyboard.add(key_no);
        question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?';
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)



bot.infinity_polling(none_stop=True, interval=0)