#!/usr/bin/env python3
""" An Async coroutine that takes in an integer arg, that waits for
a random delay (0, max_delay) seconds"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait random"""
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
