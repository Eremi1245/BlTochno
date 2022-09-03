from datetime import datetime

from BlTochno.DataBase.models import Event
from BlTochno.DataBase.session import Sessn
from BlTochno.const import default_response

session=Sessn().get_session()

def add_event(new_event:Event)->dict:
    result=default_response
    try:
        new_event.dt=datetime.strftime()
    try:
        session.add(new_event)
        session.commit()
        result['status']=True
    except Exception as er:
        result['error']=er
    return result
