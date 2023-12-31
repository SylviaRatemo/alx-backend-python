#!/usr/bin/env python3
'''Task 2
'''
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    '''Task 2
    '''
    s = time.perf_counter()
    await wait_n(n, max_delay)
    elapsed = time.perf_counter() - s
    return elapsed / n
