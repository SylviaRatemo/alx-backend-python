#!/usr/bin/env python3
'''Task 0
'''
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    '''Task 0
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
