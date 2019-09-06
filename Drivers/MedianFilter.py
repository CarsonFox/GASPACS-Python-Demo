from collections import deque

from Drivers.Component import Component


class MedianFilter(Component):
    def __init__(self, name, delay, target):
        super().__init__(name, delay)
        self.target = target
        self.ringBuffer = deque(maxlen=10)

    def update(self, context):
        self.ringBuffer.append(context[self.target])
        context[self.name] = sum(self.ringBuffer) / len(self.ringBuffer)
