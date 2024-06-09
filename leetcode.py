import asyncio
import time

async def coro1(arg):
    await asyncio.sleep(arg)


# async def coro1(arg):
#     await asyncio.sleep(arg)


async def gather():
    start_time = time.perf_counter()
    result = await asyncio.gather(
        *[coro1(i) for i in range(1, 6)],
    )
    print(f" exec time: {time.perf_counter() - start_time}")
    return result

asyncio.run(gather())