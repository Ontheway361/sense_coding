#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2020/05/28
author: relu
"""

import time
import random
import numpy as np
from IPython import embed

def random_pivot(arr, sidx = 0, eidx = 0):
    ''' T(n) = O(n) '''
    ridx = np.random.randint(sidx, eidx, 1).item()
    pval = arr[ridx]
    arr[ridx] = arr[eidx]
    slow_idx = sidx - 1
    for fast_idx in range(sidx, eidx):

        if arr[fast_idx] <= pval:
            slow_idx += 1
            tmp = arr[slow_idx]
            arr[slow_idx] = arr[fast_idx]
            arr[fast_idx] = tmp
    arr[eidx] = arr[slow_idx + 1]
    arr[slow_idx + 1] = pval
    return slow_idx + 1


def fetch_ith_element_recursive(arr, sidx = 0, eidx = 0, ith = 1):
    ''' T(n) = O(n) '''

    if sidx == eidx:
        return arr[sidx]

    pidx = random_pivot(arr, sidx, eidx)
    nums = pidx - sidx + 1
    print('sidx : %2d, pidx : %2d\t' % (sidx, pidx), arr)
    if ith == nums:
        return arr[pidx]
    elif ith < nums:
        return fetch_ith_element_recursive(arr, sidx, pidx - 1, ith)
    else:
        return fetch_ith_element_recursive(arr, pidx + 1, eidx, ith - nums)


def fetch_ith_element_forloop(arr, ith = 1):
    ''' T(n) = O(n) '''

    sidx, eidx = 0, len(arr) - 1
    while ith > 0:

        pidx = random_pivot(arr, sidx, eidx)
        nums = pidx - sidx + 1
        if ith == nums:
            return arr[pidx]
        elif ith < nums:
            eidx = pidx - 1
            pidx = random_pivot(arr, sidx, eidx)
        else:
            sidx = pidx + 1
            pidx = random_pivot(arr, sidx, eidx)
            ith -= nums


if __name__  == "__main__":

    max_bound, v_len = 100, 20
    pick_ith = 10
    # v_list = np.random.permutation(range(max_bound)).tolist()[:v_len]
    v_list = [0, 1, 3, 7, 11, 14, 16, 17, 22, 26, 27, 40, 50, 51, 54, 55, 66, 72, 90, 91]

    print('before sorted : ', v_list)
    print('after sorted  :', sorted(v_list))
    print(fetch_ith_element_recursive(v_list, 0, v_len - 1, pick_ith))
    print(fetch_ith_element_forloop(v_list, pick_ith))
