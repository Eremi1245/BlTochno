from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from secret import CONNECT_TO_DB

engine = create_engine(CONNECT_TO_DB)

# Client1=Client('xxxmessixxx@mail.ru','Мой первый юзер')
# Client2=Client('Eremi1245','Мой второй юзер')

#открываем сессию
# with Session(engine,autoflush=True) as session:
#     try:
#         session.add(Client1)
#         session.add(Client2)
#         session.commit() #созранить изменение
#     except Exception as er:
#         print(er)
#
#     try:
#         clients = select(Client)  # это просто формирование строки запроса
#         result = session.execute(clients).all()  # а это уже ее непосредственное исполнение
#         print(result)
#     except Exception as eror1:
#         print(eror1)
# "
