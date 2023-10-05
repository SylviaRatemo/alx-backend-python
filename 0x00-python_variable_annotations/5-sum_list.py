#!/usr/bin/env python3
'''Task 5
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Complex types
    '''
    sum = 0
    for x in input_list:
        sum += x
    return sum
