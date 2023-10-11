from typing import Generator

#type hint for the generator, three arguments;
# int - represent the type of values produced
# None - type of values that can be sent into the generator(None means no sending values)
# None - value the generator returns when it's closed
# my_gen() simple generator function that yields integers
def my_gen() -> Generator[int, None, None]:
    for i in range(5):
        yield i

#implementation of the generator with type hint
gen: Generator[int, None, None] = my_gen()

for value in gen:
    print(value)