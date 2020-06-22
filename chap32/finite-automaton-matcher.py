#!/usr/bin/env python3
#-*- coding:utf-8 -*-
"""
Created on 2020/06/18
author: relu
"""


def isSuffix(prefix_str = '', src_str = ''):
    ''' test whether prefix_str if the suffix of src_str '''
    pstr_len = len(prefix_str)
    return prefix_str == src_str[-pstr_len:]


def compute_transition(pstr = '', alphaset = []):
    ''' preprocess for transition function '''

    plen, aslen = len(pstr), len(alphaset)
    transfunc = [[0] * aslen for i in range(plen + 1)]
    for q in range(plen + 1):

        for cidx in range(aslen):

            k = min(plen, q + 1)  # record already matched char
            char = alphaset[cidx]
            while k > 0 and not isSuffix(pstr[:k], pstr[:q] + char):
                k -= 1
            transfunc[q][cidx] = k
    return transfunc


def printMatrix(matrix = []):

    nrows = len(matrix)
    for ridx in range(nrows):
        print(' '.join([str(i) for i in matrix[ridx]]))


def finite_auto_matcher(src_str = '', tar_str = ''):
    ''' use finite automaton matcher to match the str '''

    match_flag = False
    tstr_len   = len(tar_str)
    alphaset   = sorted(list(set(src_str + tar_str)))
    print('alphaset : ', alphaset)
    transfunc  = compute_transition(tar_str, alphaset)
    printMatrix(transfunc)
    inital_s   = 0
    idx  = 0
    for char in src_str:

        cidx = alphaset.index(char)
        s = transfunc[inital_s][cidx]
        if s == tstr_len:
            match_flag = True
            break
        inital_s = s
        idx += 1
    return match_flag, idx


if __name__ == "__main__":

    # sstr = 'Yahoo machine learning, deep learning'
    # tstr = 'deep'
    sstr = 'abcdefghijk'
    tstr = 'hij'
    match_flag, idx  = finite_auto_matcher(sstr, tstr)
    if not match_flag:
        print('matching failed ...')
    else:
        start_idx = idx - len(tstr) + 1
        print('start-idx : %d, str : %s' % (idx, sstr[start_idx:idx+1]))
