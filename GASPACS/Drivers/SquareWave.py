from GASPACS.Drivers.Driver import Driver


class SquareWave(Driver):
    def __init__(self):
        super().__init__("SquareWave", .25)
        self.x = -1

    def update(self):
        self.x *= -1
        return self.x + 4
