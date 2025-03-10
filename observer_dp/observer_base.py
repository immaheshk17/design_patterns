from abc import ABC, abstractmethod

class ObserverBase(ABC):

    @abstractmethod
    def update(self, message):
        pass