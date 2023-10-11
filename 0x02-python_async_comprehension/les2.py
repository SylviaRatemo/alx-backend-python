import asyncio

result = []
async for i in aiter():
    if i % 2:
        result.append(i)

result = [i async for i in aiter() if i % 2]


#synchronous list comprehension
squares = [x**2 for x in range(5)]

#async list comprehension
async_squares = [x**2 async for x in some_async_generator()]

#synchronous set comprehension
squares_set = {x**2 for x in range(5)}

#async set comprehension
async_squares_set = {x**2 async for x in some_async_generator()}

#synchronous dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}

#asynchronous dictionary comprehension
async_squares_dict = {x: x**2 async for x in some_async_gen()}

