import asyncio

from Drivers import *


async def startLoop():
    context = {}
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
