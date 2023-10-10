#!/usr/bin/env python3
'''Task 0
'''
import random
import asyncio


async def wait_random(max_delay: int = 1) -> float:
    '''Task 0
    '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
