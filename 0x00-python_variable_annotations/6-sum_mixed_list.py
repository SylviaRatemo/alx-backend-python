#!/usr/bin/env python3
'''Task 6
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    '''Complex types - Mixed list
    '''
    sum = 0.0
    for x in mxd_lst:
        sum += x
    return sum
