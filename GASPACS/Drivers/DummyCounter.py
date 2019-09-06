from GASPACS.Drivers.Driver import Driver


class DummyCounter(Driver):
    def __init__(self):
        super().__init__("Counter", 0.5)
        self.x = 0

    def update(self):
        self.x += 1
        return self.x
