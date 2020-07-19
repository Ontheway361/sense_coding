#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2020/06/09
author: relu
"""

import numpy as np
from IPython import embed


def gen_number_triangle(nrows = 1, maxNum = 99):
    ''' generate the number-triangle '''
    triangle = []
    for ridx in range(1, nrows + 1):
        triangle.append(np.random.randint(1, maxNum, ridx).tolist())
    return triangle

def maxSum(triangle):
    '''
    find the route with max sum
    status-transfer formula:
    if ridx = len(triangle) - 1:
        MaxSum(r,j) = D(r,j)
    else:
        MaxSum( r, j) = Max{ MaxSum(r＋1,j), MaxSum(r+1,j+1) } + D(r,j)
    '''
    nrows  = len(triangle)
    MaxSum = [[0] * i for i in range(1, nrows + 1)]
    solution = [0] * nrows
    for ridx in range(nrows - 1, -1, -1):

        if ridx == nrows - 1:
            for cidx in range(ridx + 1):
                MaxSum[ridx][cidx] = triangle[ridx][cidx]
        else:
            for cidx in range(ridx + 1):
                MaxSum[ridx][cidx] = max(MaxSum[ridx + 1][cidx], MaxSum[ridx + 1][cidx + 1]) + triangle[ridx][cidx]
    maxidx = 0
    for ridx in range(nrows):

        if ridx == 0:
            solution[ridx] = triangle[0][maxidx]
        else:
            maxval = max(MaxSum[ridx][maxidx], MaxSum[ridx][maxidx+1])
            maxidx = MaxSum[ridx].index(maxval)
            solution[ridx] = triangle[ridx][maxidx]
    return solution


def printTriangle(triangle):
    ''' print triangle-info '''
    nrows = len(triangle)
    for ridx in range(nrows):
        print(' '.join([str(i) for i in triangle[ridx]]) + '\n')

if __name__ == '__main__':

    triangle = gen_number_triangle(11)
    solution = maxSum(triangle)
    printTriangle(triangle)
    # printTriangle(MaxSum)
    print(solution, sum(solution))
