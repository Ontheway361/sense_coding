#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2020/05/06
author: relu
"""

import time
import random
import numpy as np

from IPython import embed

def findTargetSumPair_v1(arr, sumval):
    '''
    时间复杂度 ：T(n) = O(nlogn) + O(n) | nlogn
    空间复杂度 ：S(n) = O(1)
    核心思想  ：只要pair之和不等于目标值，leftidx和rightidx之间的距离就会减小！
    '''
    arr = sorted(arr)  # arr = np.sort(arr, axis=-1, kind='quicksort')
    leftidx, rightidx = 0, len(arr) - 1
    while(leftidx < rightidx):

        if arr[leftidx] + arr[rightidx] == sumval:
            # print('%d = %d + %d' % (sumval, arr[leftidx], arr[rightidx]))
            return True

        if arr[leftidx] + arr[rightidx] < sumval:
            leftidx += 1
        else:
            rightidx -= 1
    return False

def findTargetSumPair_v2(arr, sumval):
    '''
    时间复杂度 ： T(n) = O(n)
    空间复杂度 ： S(n) = O(n)
    利用字典查找键
    '''
    temp_dict = {}
    for i in arr:
        if i in temp_dict.keys():
            temp_dict[i] += 1
        else:
            temp_dict[i] = 0
    for i in arr:
        if sumval - i in temp_dict.keys():
            if (i * 2 != sumval) or (i * 2 == sumval and temp_dict[i] > 0):
                # print('%d = %d + %d' % (sumval, i, sumval-i))
                return True
    return False


if __name__  == "__main__":

    test_time = 1000000
    total_v1, total_v2 = 0, 0
    for i in range(test_time):

        arr = np.random.randint(-1000, 1000, 100)
        start_time = time.time()
        v1ans = findTargetSumPair_v1(arr, 5)
        finv1_time = time.time()
        v2ans = findTargetSumPair_v2(arr, 5)
        finv2_time = time.time()
        total_v1 += finv1_time - start_time
        total_v2 += finv2_time - finv1_time
    print('v1-time : %d sec, v2-time : %d sec' % (total_v1, total_v2))
