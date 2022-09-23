from enum import Enum
from django.db import models

status_choise=[
    ('ACTIVE',"Запланированно"),
    ('SUCCES' ,"Успешно выполненное"),
    ('NO_SUCCES' ,"Не выполненное"),
    ('PENDING' ,'Отложенное'),
    ('CANCEL' ,'Отмененно'),
    ('In processing','Выполняется'),
    ('passed','Прошло'),
    ]


status_choise_for_tag_filter={
    'ACTIVE':"Запланированно",
    'SUCCES' :"Успешно выполненное",
    'NO_SUCCES' :"Не выполненное",
    'PENDING' :'Отложенное',
    'CANCEL' :'Отмененно',
    'In processing':'Выполняется'
}