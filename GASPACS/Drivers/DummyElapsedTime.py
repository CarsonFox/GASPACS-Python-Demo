from datetime import datetime

from GASPACS.Drivers.Driver import Driver


class DummyElapsedTime(Driver):
    def __init__(self):
        super().__init__("ElapsedTime", 1)
        self.initialTime = datetime.now()

    def update(self):
        print((datetime.now() - self.initialTime).seconds, "seconds elapsed")
        return (datetime.now() - self.initialTime).seconds
