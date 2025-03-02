from concrete_builder import GamingBuilder


class Director:
    # Director gets the requirement from the client.
    def __init__(self):
        self.gaming_builder = GamingBuilder()

    def construct_gaming(self, cpu, gpu, ram, ssd):
        return self.gaming_builder.set_cpu(cpu).set_gpu(gpu).set_ram(ram).set_ssd(ssd).build()

