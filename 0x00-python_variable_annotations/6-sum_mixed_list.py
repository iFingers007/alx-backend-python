#!/usr/bin/env python3
'''Module for Complex types - list of floats'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    '''sums a list and gives the sum as return
    Arguments:
    mxd_lst: list inputed
    '''
    return float(sum(mxd_lst))
