from setuptools.config.pyprojecttoml import validate

from builder import ComputerBuilder
from computer import Computer

class GamingBuilder(ComputerBuilder):
    def __init__(self):
        self.ram = None
        self.cpu = None
        self.gpu = None
        self.ssd = None


    def set_cpu(self, cpu):
        self.cpu = cpu
        return self

    def set_gpu(self, gpu):
        self.gpu = gpu
        return self

    def set_ram(self, ram):
        self.ram = ram
        return self

    def set_ssd(self, ssd):
        self.ssd = ssd
        return self

    def validate(self):
        if self.ram < 8:
            raise Exception("Low Ram")

        if self.ssd < 256:
            raise Exception("Low SSD")

        if self.gpu < 4:
            raise Exception("Low GPU")

        if self.cpu < 8:
            raise Exception("Low CPU processor")

    def build(self):
        self.validate()
        return Computer(self.ram, self.cpu, self.gpu, self.ssd)

