#!/usr/bin/env python3
''' Module for 4-tasks.py'''

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Take the code from wait_n and alter it into a new function task_wait_n
    Args:
    n: Number of times
    max_delay: Maximum delay
    '''
    # Create list of asyncio.Tasks
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    # Gather all tasks and wait for them to complete
    delays = await asyncio.gather(*tasks)
    return sorted(delays)  # Return delays sorted in ascending order
