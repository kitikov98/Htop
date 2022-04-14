from abc import ABC, abstractmethod

class Parent(ABC):
    info = {}
    template =""

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def prepare(self):
        pass

    def show(self):
        print(self.template.format(**self.info))

