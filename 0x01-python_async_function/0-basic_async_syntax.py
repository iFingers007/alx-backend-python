#!/usr/bin/python3
'''Module for 0. The basics of async'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Asynchronous function that returns delay
    Arguments:
    max_delay = random maximum delay)
    '''
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
