#!/usr/bin/env python3
#-*- coding:utf-8 -*-
"""
Created on 2020/06/17
author: relu
"""

import numpy as np
from IPython import embed

def RabinKarp(src_str, tar_str, d = 10, q = 13):

    slen, tlen = len(src_str), len(tar_str)
    h = np.power(d, tlen - 1) % q
    pval, tval = 0, 0
    for i in range(tlen):
        pval = (d * pval + int(tar_str[i])) % q
        tval = (d * tval + int(src_str[i])) % q

    match_idx = None
    for i in range(slen-tlen):

        if pval == tval:
            match_flag = True
            for k in range(tlen):
                if src_str[i+k] != tar_str[k]:
                    match_flag = False
                    break
            if match_flag:
                match_idx = i
                break
        tval = (d * (tval - int(src_str[i]) * h) + int(src_str[i + tlen])) % q
    return match_idx


if __name__ == "__main__":

    tstr = '123'
    for k in range(100):

        sstr = ''.join([str(i) for i in np.random.randint(0, 100, 20)])
        idx  = RabinKarp(sstr, tstr)
        print('sstr : %s' % sstr)
        if idx is None:
            print('matching failed ...')
        else:
            print('start-idx : %d, str : %s' % (idx, sstr[idx:idx+len(tstr)]))
