#!/usr/bin/env python3
'''Task 7
'''
from typing import Sequence, Tuple, List


def element_length(lst: Sequence) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
