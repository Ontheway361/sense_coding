#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2020/08/05
author: relu
"""
import random
import numpy as np
from IPython import embed

def trans_adjmat_to_adjlinkedlist(adjmat):
    adjlinkedlist = [[] for i in range(len(adjmat))]
    for nodeidx in range(len(adjmat)):
        for adjidx in range(len(adjmat)):
            if nodeidx == adjidx:
                continue
            if adjmat[nodeidx, adjidx]:
                adjlinkedlist[nodeidx].append(adjidx)
    print(adjmat)
    print(adjlinkedlist)
    return adjlinkedlist

def gen_adjmat(num_node = 5):
    adjmat = np.triu(np.random.randn(num_node, num_node))
    adjmat += adjmat.T - np.diag(adjmat.diagonal())
    print(adjmat)
    adjmat = np.where(adjmat > 0, 1, 0)
    row, col = np.diag_indices_from(adjmat)
    adjmat[row, col] = 1
    return adjmat


if __name__ == "__main__":

    num_node = 7
    np.random.seed(0)
    adjmat = gen_adjmat(num_node)
    adjlinkedlist = trans_adjmat_to_adjlinkedlist(adjmat)
