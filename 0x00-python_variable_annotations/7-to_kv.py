#!/usr/bin/env python3
'''Module for Complex types - list of floats'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''sums a list and gives the sum as return
    Arguments:
    mxd_lst: list inputed
    '''
    return (k, v ** 2)
