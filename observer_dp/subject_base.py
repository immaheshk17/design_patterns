from abc import ABC, abstractmethod

class SubjectBase(ABC):

    @abstractmethod
    def change(self, update):
        pass

    @abstractmethod
    def attach(self, new_observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass
