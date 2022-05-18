#!/usr/bin/env python3
""" Async Comprehension """

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """create a List with 10 number random

    Returns:
        List[float]: a list with result of async generator method
    """
    return [number async for number in async_generator()]
