from datetime import datetime

from Drivers.Driver import Driver


class DummyElapsedTime(Driver):
    def __init__(self):
        super().__init__("ElapsedTime", 1)
        self.initialTime = datetime.now()

    def update(self):
        return (datetime.now() - self.initialTime).seconds
