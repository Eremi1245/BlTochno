from copy import deepcopy

from sqlalchemy import Column, Integer, String, create_engine, DateTime, ForeignKey, VARCHAR, Date, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# from db_setup import Base

from .db_setup import Base


class Category(Base):
    __tablename__ = 'categories' #название таблицы
    id = Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String(120))

class Event(Base):
    __tablename__ = 'events' #название таблицы
    id = Column(Integer, primary_key=True, autoincrement=True)
    category=Column(Integer,ForeignKey("categories.id"))
    name = Column(String(120))
    dt=Column(Date)
    tm=Column(Time)
    desc = Column(String(120))

class Habit(Base):
    __tablename__ = 'habits' #название таблицы
    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(Integer, ForeignKey("categories.id"))
    name=Column(String(120))

class Habits_Events(Base):
    __tablename__ = 'habits_events' #название таблицы
    id = Column(Integer, primary_key=True, autoincrement=True)
    habit_id=Column(Integer,ForeignKey("habits.id"))
    event_id = Column(Integer, ForeignKey("events.id"))

class HookaCategory(Base):
    __tablename__ = 'hooka_categories' #название таблицы
    id = Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String(120))

class HookaComponent(Base):
    __tablename__ = 'hooka_components' #название таблицы
    id = Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String(120))
    category=Column(Integer, ForeignKey("hooka_categories.id"))


class HookaComponentAnalogs(Base):
    __tablename__ = 'hooka_component_analogs' #название таблицы
    id = Column(Integer, primary_key=True, autoincrement=True)
    main_component=Column(Integer, ForeignKey("hooka_components.id"))
    analog_component=Column(Integer, ForeignKey("hooka_components.id"))


class HookaMixRecept(Base):
    __tablename__ = 'hooka_mix_recepts' #название таблицы
    id = Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String(120))
    component=Column(Integer, ForeignKey("hooka_components.id"))
    desc=Column(String(120))
