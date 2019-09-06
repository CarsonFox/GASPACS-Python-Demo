import asyncio

from GASPACS.Drivers.ContextPrinter import ContextPrinter
from GASPACS.Drivers.DummyCounter import DummyCounter
from GASPACS.Drivers.DummyElapsedTime import DummyElapsedTime
from GASPACS.Drivers.MedianFilter import MedianFilter
from GASPACS.Drivers.SquareWave import SquareWave

context = {}


async def startLoop():
    lock = asyncio.Lock()
    await asyncio.gather(
        *map((lambda x: x.run(context, lock)), [
            DummyElapsedTime(),
            DummyCounter(),
            SquareWave(),
            MedianFilter("SquareWaveFilter", .25, "SquareWave"),
            ContextPrinter()]
             ))


asyncio.run(startLoop())
