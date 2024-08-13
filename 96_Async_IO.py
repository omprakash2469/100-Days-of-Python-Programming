"""
Async IO
--
Asynchronous I/O, or async for short, is a programming pattern that allows for high-performance I/O operations in a concurrent and non-blocking manner. In Python, async programming is achieved through the use of the asyncio module and asynchronous functions.

"""

import asyncio

async def my_func():
    await asyncio.sleep(1)
    return "Hello Async World!"

async def main():
    result = await my_func()
    print(result)

asyncio.run(main())