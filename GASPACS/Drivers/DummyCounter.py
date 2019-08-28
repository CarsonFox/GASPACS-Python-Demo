from GASPACS.Drivers.Driver import Driver


class DummyCounter(Driver):
    def __init__(self):
        super().__init__("ElapsedTime", 0.5)
        self.c = 0

    def update(self):
        self.c += 1
        print(self.c)
        return self.c
