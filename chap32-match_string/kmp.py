#!/usr/bin/env python3
#-*- coding:utf-8 -*-
"""
Created on 2020/07/01
author: relu
"""

from IPython import embed

def calculate_prefixtable_speedup(pstr = ''):
    '''
    k : 当前匹配操作前，已经匹配的最大前缀串的长度
    '''
    prefix = [0] * len(pstr)
    k = 0
    for q in range(1, len(pstr)):

        while k > 0 and pstr[k] != pstr[q]:
            k = prefix[k-1]
        if pstr[k] == pstr[q]:
            k += 1
        prefix[q] = k
    return prefix

def kmp(sstr = '', pstr = ''):
    pi = compute_prefix_func(pstr)
    slen, plen = len(sstr), len(pstr)
    q = 0
    occur_idx = []
    for i in range(slen):

        while q > 0 and pstr[q] != sstr[i]:
            q = pi[q-1]
        if pstr[q] == sstr[i]:
            q += 1
        print('i = %d, q = %d' % (i, q-1))
        if q == plen:
            occur_idx.append(i-plen+1)
            q = pi[q-1]
    return occur_idx


if __name__ == "__main__":

    pstr = 'abaabab'
    # pstr = 'abcabcabcb'
    speedup = calculate_prefixtable_speedup(pstr)
    print('speedup : ', speedup)
    # occidx = kmp(sstr, tstr)
    # if len(occidx) < 1:
    #     print('NO MATCHING')
    # else:
    #     for idx in occidx:
    #         print('pstr occurs at %d' % idx)
