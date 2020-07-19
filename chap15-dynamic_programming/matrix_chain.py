#!/usr/bin/env python3
#-*- coding:utf-8 -*-
"""
Created on 2020/06/10
author: relu
"""

import numpy as np
from IPython import embed


def matrix_chain_order(chain = []):
    ''' matrix chain order '''

    chain_len = len(chain) - 1
    qmatrix = np.zeros((chain_len, chain_len))
    splitid = np.zeros((chain_len, chain_len))

    for sub_s in range(2, chain_len + 1):

        for sidx in range(1, chain_len - sub_s + 2):

            eidx = sidx + sub_s - 1
            qmatrix[sidx-1][eidx-1] = float('inf')
            for k in range(sidx, eidx):

                qval = qmatrix[sidx-1][k-1] + qmatrix[k][eidx-1] + chain[sidx-1] * chain[k] * chain[eidx]
                if qmatrix[sidx-1][eidx-1] > qval:
                    qmatrix[sidx-1][eidx-1] = qval
                    splitid[sidx-1][eidx-1] = k
    return qmatrix, splitid


def matrix_chain_order_v2(p):
    n = len(p) - 1
    m = np.zeros((n, n))
    s = np.zeros((n, n))

    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i + l -1
            m[i-1][j-1] = float('inf')

            for k in range(i, j):
                q = m[i-1][k-1] + m[k][j-1] + p[i-1] * p[k] * p[j]
                if q < m[i-1][j-1]:
                    m[i-1][j-1] = q
                    s[i-1][j-1] = k

    return m, s


def printMatrix(matrix = []):

    nrows = len(matrix)
    for ridx in range(nrows):
        print(' '.join([str(i)+'\t' for i in matrix[ridx]]))


def print_optimal_parens(s, i, j):
    if i == j:
        print('A', i, sep='',end='')
    else:
        print('(', end='')
        print_optimal_parens(s, i, int(s[i-1][j-1]))
        print_optimal_parens(s, int(s[i-1][j-1])+1, j)
        print(')', end='')


if __name__ == "__main__":

    chain_len = 7
    chain = np.random.randint(5, 20, chain_len + 1)
    # chain = np.array([5, 10, 3, 12, 5, 50, 6])
    print(chain)
    qmatrix, splitid = matrix_chain_order(chain)
    m, s = matrix_chain_order_v2(chain)

    printMatrix(qmatrix)
    print('\n')
    printMatrix(splitid)
    print_optimal_parens(splitid, 1, chain_len)

    print('\n')
    printMatrix(m)
    print('\n')
    printMatrix(s)
    print_optimal_parens(s, 1, chain_len)
