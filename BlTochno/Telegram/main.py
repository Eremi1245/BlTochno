from copy import deepcopy
from datetime import datetime
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
from telebot import TeleBot, types
from BlTochno.other.supportive_classes import Singleton
from secret import TOKEN


def main():
    bot = TeleBot(TOKEN)
    tg_commands=[
        '/my_day',
        '/my_week',
        '/add_event',
        '/add_category'
    ]

    # event=Event()

    @bot.message_handler(commands=['start'])
    def bot_start(message):
            all_commands='\n'.join(tg_commands)
            bot.send_message(message.from_user.id, all_commands)

    # @bot.message_handler(commands=['my_day'])
    # def get_my_day(message):
    #     ma_day=my_day(Event)
    #     answer='\n'.join([f'{i+1}.{ma_day[i].name} ({ma_day[i].desc}) - {ma_day[i].tm}' for i in range(len(ma_day))])
    #     bot.send_message(message.from_user.id, answer)

    # @bot.message_handler(commands=['my_week'])
    # def get_my_week(message):
    #     bot.send_message(message.from_user.id, 'Расписание на неделю')

    # @bot.message_handler(commands=['add_event'])
    # def add_event(message):
    #     global event
    #     event=Event()
    #     bot.send_message(message.from_user.id, 'Введите название евента')
    #     bot.register_next_step_handler(message, event_name)

    # @bot.message_handler(commands=['event_name'])
    # def event_name(message):
    #     name=message.text
    #     event.name=name
    #     bot.send_message(message.from_user.id, 'Введите дату ивента')
    #     calendar(message)

    # @bot.message_handler(commands=['event_time'])
    # def event_time(message):
    #     tm=message.text + ':00'
    #     tm=datetime.strptime(tm, "%H:%M:%S").time()
    #     event.tm=tm
    #     categories = get_object(Category)
    #     keyboard = types.InlineKeyboardMarkup()
    #     for categ in categories:
    #         key = types.InlineKeyboardButton(text=categ.name, callback_data=categ.id)
    #         keyboard.add(key)
    #     bot.send_message(message.from_user.id, text='Укажите категорию ивента', reply_markup=keyboard)
    #     bot.send_message(message.from_user.id, 'Описание ивента')
    #     bot.register_next_step_handler(message, event_desc)

    # @bot.message_handler(commands=['event_desc'])
    # def event_desc(message):
    #     desc=message.text
    #     event.desc=desc
    #     result=add_to_data(event)
    #     if result["status"]:
    #         bot.send_message(message.from_user.id, 'Евент добавлен')
    #     else:
    #         bot.send_message(message.from_user.id, f'Ошибка: {result["error"]}')

    # @bot.message_handler(commands=['calendar'])
    # def calendar(m):
    #     calendar, step = DetailedTelegramCalendar(calendar_id=1).build()
    #     bot.send_message(m.chat.id,
    #                     f"Select {LSTEP[step]}",
    #                     reply_markup=calendar)

    # @bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id=1))
    # def cal(c):
    #     min_date = datetime.today().date()
    #     print(min_date)
    #     result, key, step = DetailedTelegramCalendar(calendar_id=1,locale='ru',min_date=min_date).process(c.data)
    #     if not result and key:
    #         bot.edit_message_text(f"Select {LSTEP[step]}",
    #                             c.message.chat.id,
    #                             c.message.message_id,
    #                             reply_markup=key)
    #     elif result:
    #         bot.edit_message_text(f"You selected {result}",
    #                             c.message.chat.id,
    #                             c.message.message_id)
    #         event.dt = result
    #         bot.send_message(c.from_user.id, 'Введите время ивента')
    #         bot.register_next_step_handler(c.message, event_time)

    # @bot.callback_query_handler(func=lambda call: True)
    # def callback_worker(call):
    #     id=call.data
    #     event.category=id

    print('Запускаем телеграмм....')
    bot.infinity_polling(none_stop=True, interval=0)

if __name__ == '__main__':
    main()
else:
    main
