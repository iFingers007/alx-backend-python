#!/usr/bin/env python3
'''Module for Async Generator'''
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    '''Async generator function'''
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
