from datetime import datetime

from sqlalchemy import select

from BlTochno.DataBase.session import Sessn
from BlTochno.const import default_response

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


def get_object(desired_object):
    try:
        result = select(desired_object)  # это просто формирование строки запроса
        result = session.execute(result).all()  # а это уже ее непосредственное
        result=[res[0] for res in result]
        return result
    except Exception as er:
        print(er)