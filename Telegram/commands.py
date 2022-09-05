from copy import deepcopy
from datetime import datetime

from sqlalchemy import select

from BlTochno.DataBase.session import Sessn
from BlTochno.const import default_response
from BlTochno.other.supportive_classes import Singleton

session=Sessn().get_session()

def add_to_data(new_object)->dict:
    result=default_response
    try:
        session.add(new_object)
        session.commit()
        result['status']=True
    except Exception as er:
        result['error']=er
    return result


def get_object(desired_object,**kwargs):
    if kwargs:
        try:
            result = select(desired_object).where(desired_object.id==kwargs["id"])
            result = session.execute(result) # а это уже ее непосредственное
            result=[res[0] for res in result]
            return result
        except Exception as er:
            print(er)
    else:
        try:
            result = select(desired_object)  # это просто формирование строки запроса
            result = session.execute(result).all()  # а это уже ее непосредственное
            result=[res[0] for res in result]
            return result
        except Exception as er:
            print(er)


# class Add_Object_Controller(metaclass=Singleton):
#
#
#     def __init__(self,obj):
#         self.obj=obj
#         self.attrs={}
#         self.get_obj_attrs()
#
#
#     def get_obj_attrs(self):
#         fields=deepcopy(self.obj.__dict__['_sa_instance_state']['unloaded'])
#         values=[None*len(fields)]
#         self.attrs=dict(zip(fields,values))
#         try:
#             del self.attrs['id']
#         except Exception as er:
#             print(f'В классе {self.obj.__tablename__} нет атрибута id!!!')
#
#     def start(self,messages,name_value_attributes:dict):
#         attrib_name=name_value_attributes['attrib_name']
#         attrib_value=name_value_attributes['attrib_value']
#         for atrib,value in self.attrs.items():
#             if not value:
#                 name_value_attributes.update({'attrib_name': atrib})
#                 bot.send_message(message.from_user.id, 'Введите название евента')
#                 bot.register_next_step_handler(message, add_event, args)
#         elif not new_event.dt:
#             args.update({'attribute': 'dt'})
#             bot.send_message(message.from_user.id, 'Введите Дату ивента')
#             bot.register_next_step_handler(message, add_event, args)
#         elif not new_event.tm:
#             args.update({'attribute': 'tm'})
#             bot.send_message(message.from_user.id, 'Введите Время ивента')
#             bot.register_next_step_handler(message, add_event, args)
#         elif not new_event.category:
#             args.update({'attribute': 'category'})
#             categories = get_object(Category)
#             keyboard = types.InlineKeyboardMarkup()
#             for categ in categories:
#                 key = types.InlineKeyboardButton(text=categ.name, callback_data=categ.id)
#                 keyboard.add(key)
#             question = 'Выбери id категории ивента'
#             bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
#         elif not new_event.desc:
#             args.update({'attribute': 'desc'})
#             bot.send_message(message.from_user.id, 'Введите описание ивента\nВведите "нет" если описание не требуется')
#             bot.register_next_step_handler(message, add_event, args)
#         else:
#             result = add_to_data(new_event)
#             if result["status"]:
#                 bot.send_message(message.from_user.id, 'Евент добавлен')
#             else:
#                 bot.send_message(message.from_user.id, f'Ошибка: {result["error"]}')

