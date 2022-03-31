#!/usr/bin/env python3
"""  Python Annotation """

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return a value"""
    return [(i, len(i)) for i in lst]
