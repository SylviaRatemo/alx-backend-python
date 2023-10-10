#!/usr/bin/env python3
'''Task 1
'''
import random
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 1) -> float:
    '''Task 1
    '''
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return ([min(delays[:1+1], default=float('inf'))
             for i in range(len(delays))])
