#!/usr/bin/env python3
'''Task 9
'''
from typing import Sequence, Tuple, List, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' iterable object
    '''
    return [(i, len(i)) for i in lst]
