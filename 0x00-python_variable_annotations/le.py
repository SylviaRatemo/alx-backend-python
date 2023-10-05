from typing import Callable


def foo() -> Callable[[int, int], int]:
    func: Callable[[int, int], int] = lambda x, y: x + y
    return func
print(foo())