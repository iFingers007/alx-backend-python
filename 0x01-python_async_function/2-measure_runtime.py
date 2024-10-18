#!/usr/bin/env python3
'''Module for Measure the runtime'''

import time
import asyncio
from typing import Callable

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n.

    Args:
    n: number of times
    max_delay: Maximum Delay
    '''
    start_time = time.perf_counter()  # Record the start time
    asyncio.run(wait_n(n, max_delay))  # Run the wait_n coroutine
    end_time = time.perf_counter()  # Record the end time

    total_time = end_time - start_time  # Calculate total execution time
    return total_time / n  # Return average time per coroutine
