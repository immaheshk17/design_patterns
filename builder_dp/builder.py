from abc import ABC, abstractmethod

class ComputerBuilder(ABC):

    @abstractmethod
    def set_gpu(self, gpu):
        pass

    @abstractmethod
    def set_cpu(self, cpu):
        pass

    @abstractmethod
    def set_ram(self, ram):
        pass

    @abstractmethod
    def set_ssd(self, ssd):
        pass

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def build(self):
        pass
