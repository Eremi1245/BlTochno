# from copy import deepcopy
# from datetime import datetime
import json
import requests
from requests import Response
# from sqlalchemy import select

# from BlTochno.BlTochno.DataBase.session import Sessn
# from BlTochno.BlTochno.const import default_response
# from BlTochno.BlTochno.other.supportive_classes import Singleton

# session=Sessn().get_session()

# def add_to_data(new_object)->dict:
#     result=default_response
#     try:
#         session.add(new_object)
#         session.commit()
#         result['status']=True
#     except Exception as er:
#         result['error']=er
#     return result

# def get_object(desired_object,**kwargs):
#     if kwargs:
#         try:
#             result = select(desired_object).where(desired_object.id==kwargs["id"])
#             result = session.execute(result) # а это уже ее непосредственное
#             result=[res[0] for res in result]
#             return result
#         except Exception as er:
#             print(er)
#     else:
#         try:
#             result = select(desired_object)  # это просто формирование строки запроса
#             result = session.execute(result).all()  # а это уже ее непосредственное
#             result=[res[0] for res in result]
#             return result
#         except Exception as er:
#             print(er)

from urllib import request


def my_day():
    result = ''
    try:
        resp = requests.get('http://127.0.0.1:8000/api/events/')
        resp = request_handler(resp)
        for res in resp:
            result += f'{res["tm_start"]} - {res["name"]} ({res["status"]})\n'
        return result
    except Exception as er:
        print(er)


def request_handler(request: Response):
    request = eval(request.text)
    return request
