#!/usr/bin/env python3
#-*- coding:utf-8 -*-
"""
Created on 2020/06/19
author: relu
"""

from IPython import embed

def compute_prefix_func(pstr = ''):

    func = [0] * len(pstr)
    for q in range(1, len(pstr)):
        # pi[q] = max{k: k < q & P[:k] --> P[:q]}
        if func[q-1] > 0 and pstr[q] == pstr[func[q-1]]:
            func[q] = func[q-1] + 1
        else:
            k = 0
            while k < q and pstr[:k+1] == pstr[:q+1][-(k+1):]:
                k += 1
            func[q] = k
    return func


def kmp(sstr = '', pstr = ''):
    pass


if __name__ == "__main__":

    # sstr = 'Yahoo machine learning, deep learning'
    # tstr = 'deep'
    sstr = 'abcdefghijk'
    # tstr = 'ababaca'
    tstr = 'abbaabaccaba'
    func  = compute_prefix_func(tstr)
    print(func)
