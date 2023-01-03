

from customer import Customer
from option import Option


class Message:
    def __init__(self, option: Option, obj: Customer) -> None:
        self.option = option
        self.obj = obj
    
    def getOption(self) -> Option:
        return self.option

    def getObj(self) -> Customer:
        return self.obj