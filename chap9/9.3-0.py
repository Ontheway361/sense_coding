#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2020/05/29
author: relu
"""


def partition_with_median(arr, sidx = 0, eidx = 0, median = 0):
    ''' T(n) = O(n) '''

    slow_idx = sidx - 1
    for fast_idx in range(sidx, eidx + 1):

        if arr[fast_idx] <= median:
            slow_idx += 1
            tmp = arr[slow_idx]
            arr[slow_idx] = arr[fast_idx]
            arr[fast_idx] = tmp
    return slow_idx


def insertsort(arr, sidx = 0, eidx = 0):
    ''' T(n) = O(n^2) '''
    for i in range(sidx, eidx + 1):

        key = arr[i]
        idx = i - 1
        while idx >= 0 and arr[idx] > key:
            arr[idx + 1] = arr[idx]
            idx -= 1
        arr[idx + 1] = key
    midx = (sidx + eidx) // 2
    return arr[mid]


def select_ith_element(arr, ith):
    ''' T(n) = O(n) '''

    if len(arr) <= 5:
        return insertsort(arr, 0, len(arr) - 1)

    median_arr = []
    n_splits = len(arr) // 5
    n_residu = len(arr) % 5
    for i in range(n_splits):
        p_start = i * 5
        p_end   = p_start + 4
        median_arr.append(insertsort(arr, p_start, p_end))
    if n_residu > 0:
        median_arr.append(insertsort(arr, p_end + 1, p_end + n_residu))

    midx = select_ith_element(median_arr, )
