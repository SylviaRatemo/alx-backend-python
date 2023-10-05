#!/usr/bin/env python3
'''Task 7
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Complex types - string and int/float to tuple
    '''
    func: Callable[[float], int] = lambda x: x * multiplier
    return func
