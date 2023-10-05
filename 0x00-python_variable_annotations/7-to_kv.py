#!/usr/bin/env python3
'''Task 7
'''
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Complex types - string and int/float to tuple
    '''
    result = (k, float(pow(v, 2)))
    return result
