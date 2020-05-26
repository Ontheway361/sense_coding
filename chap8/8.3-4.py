#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2020/05/26
author: relu
"""
import math
import time
import random
import numpy as np
from IPython import embed

def fetch_ith_bit(n, i_th = 0, base = 10):
    return (n % np.power(base, i_th + 1)) // np.power(base, i_th)


def radixsort(arr, base = 10, pow = 3):

    arrlen = len(arr)
    arr_cp = [None] * arrlen
    for bidx in range(pow):

        hist = [0] * (base + 1)
        resv = [0] * base
        for i in range(arrlen):
            bit_num = fetch_ith_bit(arr[i], bidx, base)
            resv[i] = bit_num
            hist[bit_num] += 1
        for i in range(1, len(hist)):
            hist[i] += hist[i-1]
        for i in range(arrlen - 1, -1, -1):
            arr_cp[hist[resv[i]]-1] = arr[i]
            hist[resv[i]] -= 1
        for i in range(arrlen):
            arr[i] = arr_cp[i]
    return arr_cp


if __name__  == "__main__":

    base, pow = 12, 8
    v_list = np.random.randint(0, np.power(base, pow), base).tolist()
    print('before sorted : ', v_list)
    print('after sorted  :', radixsort(v_list, base, pow))
