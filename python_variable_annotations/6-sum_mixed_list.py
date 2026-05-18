#!/usr/bin/env python3
"""Type-annotated function sum_mixed_list."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return sum of integers and floats in a list."""
    return float(sum(mxd_lst))
