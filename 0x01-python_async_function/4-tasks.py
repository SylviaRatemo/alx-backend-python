#!/usr/bin/env python3
'''Task 4
'''
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 1) -> List[float]:
    '''Task 4
    '''
    delays = await asyncio.gather(*(task_wait_random(max_delay)
                                    for _ in range(n)))
    return ([min(delays[:1+1], default=float('inf'))
             for i in range(len(delays))])
