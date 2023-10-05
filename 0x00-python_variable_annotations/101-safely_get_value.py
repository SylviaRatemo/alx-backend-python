#!/usr/bin/env python3
'''Task 11
'''
from typing import TypeVar, Union, Any, Mapping
T = TypeVar('T')
default = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default) -> Union[Any, T]:
    ''' more type annot
    '''
    if key in dct:
        return dct[key]
    else:
        return default
