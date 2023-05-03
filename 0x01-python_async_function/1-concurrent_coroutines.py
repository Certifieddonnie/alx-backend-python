#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times"""
    tsk = []
    delays = []

    for i in range(n):
        tsk = wait_random(max_delay)
        tsk.append(task)

    for tsk in asyncio.as_completed((tsk)):
        delay = await t
        ask
        delays.append(delay)

    return delays
