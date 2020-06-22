#!/usr/bin/env python3
#-*- coding:utf-8 -*-
"""
Created on 2020/06/16
author: relu
"""
from IPython import embed

def naive_string_matcher(sstr = '', tstr = ''):
    ''' test whether tstr in sstr '''
    start_idx = None
    if len(tstr) > len(sstr):
        start_idx = -1
    else:
        slen, tlen = len(sstr), len(tstr)
        for i in range(slen - tlen + 1):
            if sstr[i:(i + tlen)] == tstr:
                start_idx = i
                break
    return start_idx



def speedup_naive_string_matcher(sstr = '', tstr = ''):

    start_idx = None
    if len(tstr) > len(sstr):
        start_idx = -1
    else:
        idx, tlen = 0, len(tstr)
        while idx <= len(sstr) - len(tstr) + 1:
            iidx = 0
            while iidx < tlen and (sstr[idx+iidx] == tstr[iidx]):
                iidx += 1
            if iidx == tlen:
                start_idx = idx
                break
            idx += max(iidx, 1)

    return start_idx


if __name__ == "__main__":

    # sstr = 'Woo hoo machine-learning Yahoo| deep-learning'
    # tstr = 'hoow'
    sstr = 'aaabc'
    tstr = 'aab'
    idx  = naive_string_matcher(sstr, tstr)
    if idx is None or idx < 0:
        print('matching failed ...')
    else:
        print('start-idx : %d, str : %s' % (idx, sstr[idx:idx+len(tstr)]))

    sidx = speedup_naive_string_matcher(sstr, tstr)
    if sidx is None or sidx < 0:
        print('matching failed ...')
    else:
        print('start-idx : %d, str : %s' % (sidx, sstr[sidx:sidx+len(tstr)]))
