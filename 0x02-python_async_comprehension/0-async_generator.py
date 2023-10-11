#!/usr/bin/env python3
'''Task 0
'''
import random
import asyncio
from typing import Generator


def async_generator() -> Generator[float, None, None]:
    '''Task 0
    '''
    for i in range(10):
        asyncio.sleep(1)
        yield random.uniform(0, 10)
