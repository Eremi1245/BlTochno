from abc import ABC


class Event(ABC):


    def __init__(self,name,description):
        self.name=name
        self.description=description
        pass