#!/usr/bin/env python3
'''Task 2
'''
import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Task 2
    '''
    s = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    elapsed = time.perf_counter() - s
    return elapsed
