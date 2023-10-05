#!/usr/bin/env python3
'''Task 10
'''
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    ''' iterable object
    '''
    if lst:
        return lst[0]
    else:
        return None
