#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2020/05/31
author: relu
"""

import numpy as np
from IPython import embed


def partition(arr, sidx = 0, eidx = 0, median = 0):
    ''' T(n) = O(n) '''

    medix = 0
    for i in range(sidx, eidx + 1):

        if arr[i] == median:
            medix = i
            break
    arr[medix] = arr[eidx]
    arr[eidx]  = median
    slow_idx = sidx - 1
    for fast_idx in range(sidx, eidx):

        if arr[fast_idx] <= median:
            slow_idx += 1
            tmp = arr[slow_idx]
            arr[slow_idx] = arr[fast_idx]
            arr[fast_idx] = tmp
    arr[eidx] = arr[slow_idx + 1]
    arr[slow_idx + 1] = median
    return slow_idx + 1


def insertsort(arr, sidx = 0, eidx = 0):
    ''' T(n) = O(n^2) '''
    for i in range(sidx, eidx + 1):

        key = arr[i]
        idx = i - 1
        while idx >= sidx and arr[idx] > key:
            arr[idx + 1] = arr[idx]
            idx -= 1
        arr[idx + 1] = key
    midx = (sidx + eidx) // 2


def select(arr, left, right, k):

    if right - left <= 4:
        insertsort(arr, left, right)
        return arr[left + k - 1]

    groups = (right - left + 5) // 5
    for i in range(groups):

        low  = left + 5 * i
        high = 0
        if (low + 4) > right:
            high = right
        else:
            high = low + 4
        insertsort(arr, low, high)
        median = (low + high) // 2
        tmp = arr[left + i]
        arr[left + i] = arr[median]
        arr[median] = tmp

    pivot = select(arr, left, left + groups - 1, (1 + groups) // 2)  # Core
    mark  = partition(arr, left, right, pivot)
    pivotNumber = mark - left + 1
    if pivotNumber == k:
        return arr[mark]
    elif pivotNumber > k:
        return select(arr, left, mark - 1, k)
    else:
        return select(arr, mark + 1, right, k - pivotNumber)


if __name__  == "__main__":

    max_bound, v_len = 100, 20
    pick_ith = 5
    v_list = np.random.permutation(range(max_bound)).tolist()[:v_len]
    # v_list = [89, 8, 39, 58, 11, 75, 0, 33, 47, 57]
    print('before sorted : ', v_list)
    print('after sorted  :', sorted(v_list))
    print(select(v_list, 0, v_len - 1, pick_ith))
