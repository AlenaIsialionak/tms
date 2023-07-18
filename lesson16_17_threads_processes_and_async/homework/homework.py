import concurrent.futures as cf
import asyncio
import logging
import threading
import time

import aiohttp
import requests

from lesson16_17_threads_processes_and_async.helpers.custom_logger import setup_logging
from lesson16_17_threads_processes_and_async.homework.async_server import run_server

logger = setup_logging(__name__)
logging.getLogger('urllib3.connectionpool').setLevel('ERROR')
logging.getLogger('aiohttp.access').setLevel('ERROR')


URL = "http://0.0.0.0"
PORT = 8080
HELLO_ENDPOINT = f"{URL}:{PORT}/hello"
MAX_WORKERS = 20


def send_request():
    response = requests.get(
        url=HELLO_ENDPOINT,
        params={'requestor': threading.current_thread().name}
    )  # params is needed after Server implementation updates
    response.raise_for_status()
    data = response.json()

    return data['key'], data['value']


def using_thread(requests_count: int):
    t = time.perf_counter()
    with cf.ThreadPoolExecutor(
        max_workers=requests_count,
        thread_name_prefix='MyThread'
    ) as ex:
        futs = [ex.submit(send_request) for _ in range(requests_count)]

        done_und_undone_futs = cf.wait(
            futs, timeout=10
        )
        exec_time_1 = time.perf_counter() - t
        print(f'exec_time_1: {exec_time_1}')

        passes, fails = [], []
        for f in done_und_undone_futs.done:
            try:
                passes.append(f.result())
            except requests.exceptions.RequestException as exc:
                fails.append(exc)

        exec_time_2 = time.perf_counter() - t
        print(f'exec_time_2: {exec_time_2}')

        # NO NEED TO PARSE the Undone futures!

        # results_dict = [f.result() for f in done_und_undone_futs.done]
        # errors = [f.result() for f in done_und_undone_futs.not_done]
        # exec_time_2 = time.perf_counter() - t
        # print(f'exec_time_2: {exec_time_2}')

        print(f'passes: {passes}')
        print(f'errors: {fails}')

        assert 0 < (exec_time_2 - exec_time_1) < 2


async def send_request_async(request_number: int):  # argument is needed after Server implementation updates
    async with aiohttp.ClientSession() as session:
        async with session.get(
            url=HELLO_ENDPOINT,
            params={'requestor': f'Async_{request_number}'}  # params is needed after Server implementation updates
        ) as resp:
            resp.raise_for_status()
            await asyncio.sleep(0.7)
            data = await resp.json()

            return data['key'], data['value']


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


server = run_server(port=PORT)

using_thread(requests_count=50)

time.sleep(3)
server.kill()