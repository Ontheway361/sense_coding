#!/usr/bin/env python3
#-*- coding:utf-8 -*-
"""
Created on 2020/06/10
author: relu
"""

import numpy as np
from IPython import embed

def gen_matrix_chain(chain_len = 5):

    chain = np.random.randint(2, 10, 2 * chain_len).reshape((2, -1))
    for cidx in range(1, chain_len):
        chain[0][cidx] = chain[1][cidx-1]
    return chain


def matrix_chain_order(chain = []):
    ''' matrix chain order '''

    chain_len = len(chain[0])
    init_val  = np.prod(chain[0]) + 1
    qmatrix = [[None] * chain_len for i in range(chain_len)]
    splitid = [[None] * chain_len for i in range(chain_len)]
    for i in range(chain_len):
        qmatrix[i][i] = 0
        splitid[i][i] = 0

    for sub_s in range(2, chain_len+1):
        for sidx in range(0, chain_len - sub_s + 1):
            eidx = sidx + sub_s
            qmatrix[sidx][eidx-1] = init_val
            for k in range(sidx, eidx-1):
                qval = qmatrix[sidx][k] + qmatrix[k+1][eidx-1] + chain[0][sidx] * chain[1][k] * chain[1][eidx-1]
                if qmatrix[sidx][eidx-1] > qval:
                    qmatrix[sidx][eidx-1] = qval
                    splitid[sidx][eidx-1] = k
    return qmatrix, splitid


def printMatrix(matrix = []):

    nrows = len(matrix)
    for ridx in range(nrows):
        print(' '.join([str(i)+'\t' for i in matrix[ridx]]))


if __name__ == "__main__":

    chain_len = 5
    chain = gen_matrix_chain(chain_len)
    printMatrix(chain)
    qmatrix, splitid = matrix_chain_order(chain)
    printMatrix(qmatrix)
    print('\n')
    printMatrix(splitid)
