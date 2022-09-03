from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from BlTochno.other.supportive_classes import Singleton
from secret import CONNECT_TO_DB

engine = create_engine(CONNECT_TO_DB)

class Sessn(metaclass=Singleton):

    def __init__(self,engine:Engine=engine):
        self.engine=engine

    # def __call__(self, *args, **kwargs):
    #     session = Session(engine=self.engine,autoflush=True)
    #     return session

    def get_session(self):
        Session = sessionmaker(bind=self.engine,autoflush=True)
        session = Session()
        return session

