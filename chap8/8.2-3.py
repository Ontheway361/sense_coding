#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2020/05/26
author: relu
"""

import time
import random
import numpy as np
from IPython import embed


def countingsort_v1(arr):
    '''
    时间复杂度 ：T(n) = O(n)
    空间复杂度 ：S(n) = O(n)
    '''
    hist = [0] * (max(arr) + 1)
    arr_copy = [None] * len(arr)
    for v in arr:
        hist[v] = hist[v] + 1
    for i in range(1, len(hist)):
        hist[i] += hist[i-1]
    for index in range(len(arr)-1, -1, -1):
        val = arr[index]
        arr_copy[hist[val] - 1] = val
        hist[val] -= 1
    return arr_copy

def countingsort_v2(arr):
    '''
    时间复杂度 ：T(n) = O(n)
    空间复杂度 ：S(n) = O(n)
    '''
    length = len(arr)
    hist = [0] * (max(arr) + 1)
    arr_copy = [None] * length
    for v in arr:
        hist[v] = hist[v] + 1
    for i in range(len(hist)-1, -1, -1):
        hist[i-1] += hist[i]
    print(hist)
    for val in arr:
        arr_copy[length - hist[val]] = val
        hist[val] -= 1
    return arr_copy


if __name__  == "__main__":

    max_bound = 10
    # v_list = np.random.randint(0, max_bound, 10).tolist()
    v_list = [1, 9, 6, 5, 5, 4, 7, 9, 2, 9]
    print('before sorted : ', v_list)
    print('after sorted  :', countingsort_v2(v_list))
