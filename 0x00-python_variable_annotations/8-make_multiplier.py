#!/usr/bin/env python3
"""  Python Annotation """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return a callable"""
    def multiplciation(number: float) -> float:
        """return a multiplication"""
        return (number * multiplier)
    return multiplciation
