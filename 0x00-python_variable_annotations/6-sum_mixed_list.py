#!/usr/bin/env python3
"""  Python Annotation """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return sum list of integer and float to float"""

    return sum(mxd_lst)
