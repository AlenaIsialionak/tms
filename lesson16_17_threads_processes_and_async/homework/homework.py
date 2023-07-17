import concurrent.futures as cf
import asyncio
import time

import aiohttp
import requests

from lesson16_17_threads_processes_and_async.helpers.custom_logger import setup_logging
from lesson16_17_threads_processes_and_async.homework.async_server import run_server


logger = setup_logging(__name__)


URL = "http://0.0.0.0"
PORT = 8080
HELLO_ENDPOINT = f"{URL}:{PORT}/hello"
MAX_WORKERS = 3


def send_request():
    response = requests.get(url=HELLO_ENDPOINT)
    response.raise_for_status()
    data = response.json()

    return data['key'], data['value']


def using_thread():
    t = time.perf_counter()
    with cf.ThreadPoolExecutor(
        max_workers=MAX_WORKERS
    ) as ex:
        futs = [ex.submit(send_request) for _ in range(3)]

        done_und_undone_futs = cf.wait(
            futs, timeout=2
        )
        passes, fails = [], []
        for f in futs:
            try:
                passes.append(f.result())
            except RuntimeError as exc:
                fails.append(type(exc), str(exc))
        exec_time_1 = time.perf_counter()-t
        print(f'exec_time_1: {exec_time_1}')
        results_dict = [f.result() for f in done_und_undone_futs.done]
        errors = [f.result() for f in done_und_undone_futs.not_done]
        exec_time_2 = time.perf_counter() - t
        print(f'exec_time_2: {exec_time_2}')
        print(f'results_dict: {results_dict}')
        print(f'errors: {errors}')

        assert (exec_time_1 and exec_time_2) < 10

server = run_server(port=PORT)
using_thread()
time.sleep(5)
server.kill()

# async def send_request_async():
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url=HELLO_ENDPOINT) as resp:
#             resp.raise_for_status()
#             await asyncio.sleep(0.7)
#             data = await resp.json()
#
#             return data['key'], data['value']
#
#
# async def using_async():
#     start_time = time.perf_counter()
#     result = await asyncio.gather(
#         *[send_request_async() for i in range(3)],
#     )
#     print(f"exec time of using_async : {time.perf_counter() - start_time}")
#     return result
#
# server = run_server(port=PORT)
#
# asyncio.run(using_async())
# time.sleep(5)
# server.kill()
