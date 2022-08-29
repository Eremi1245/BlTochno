from sqlalchemy import Column, Integer, String, create_engine, DateTime, ForeignKey, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from db_setup import Base


class Events(Base):
    __tablename__ = 'events' #название таблицы
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120))
    desc = Column(String(120))


