import asyncio

from GASPACS.Drivers.DummyCounter import DummyCounter
from GASPACS.Drivers.DummyElapsedTime import DummyElapsedTime

context = {}


async def startLoop():
    lock = asyncio.Lock()
    await asyncio.gather(
        DummyElapsedTime().run(context, lock), DummyCounter().run(context, lock)
    )


asyncio.run(startLoop())
