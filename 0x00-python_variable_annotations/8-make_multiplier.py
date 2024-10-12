#!/usr/bin/env python3
'''Module for Complex types - list of floats'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''sums a list and gives the sum as return
    Arguments:
    mxd_lst: list inputed
    '''
    def mul_func(value: float) -> float:
        '''Multiplier function for the callable
        Aarguments:
        value: passed value of multiplier
        '''
        return value * multiplier
    return (mul_func)
