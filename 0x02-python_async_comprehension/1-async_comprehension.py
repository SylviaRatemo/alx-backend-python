#!/usr/bin/env python3
'''Task 1
'''
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Task 1
    '''
    result = [x async for x in async_generator()]
    return result
