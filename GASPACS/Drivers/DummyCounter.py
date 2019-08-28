from GASPACS.Drivers.Driver import Driver


class DummyCounter(Driver):
    def __init__(self):
        super().__init__("ElapsedTime", 0.5)
        self.x = 0

    def update(self):
        self.x += 1
        print("x =", self.x)
        return self.x
