from typing import TypeVar

T = TypeVar('T')

def get_item(lst: list[T], index: int) -> T:
    return lst[index]