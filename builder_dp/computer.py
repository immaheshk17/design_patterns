
class Computer:
    def __init__(self, ram, cpu, gpu, ssd):
        self.ram = ram
        self.cpu = cpu
        self.gpu = gpu
        self.ssd = ssd

    def __str__(self) -> str:
        return f"Ram: {self.ram} | CPU: {self.cpu} | DISK: {self.ssd} | GPU: {self.gpu}"