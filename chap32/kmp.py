
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
        if func[q-1] > 0 and pstr[q] == pstr[func[q-1]]:
            func[q] = func[q-1] + 1
        else:
            k = 0
            while k < q and pstr[:k+1] == pstr[:q+1][-(k+1):]:
                k += 1
            func[q] = k
    return func


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

    sstr = 'Yahoo machine learning,@deep learning deep'
    tstr = 'deep'
    sstr = 'ababaababababa'
    tstr = 'abababa'
    sstr = 'aaababababca'
    tstr = 'ababca'

    func  = compute_prefix_func(tstr)
    print(func)
    occidx = kmp(sstr, tstr)
    if len(occidx) < 1:
        print('NO MATCHING')
    else:
        for idx in occidx:
            print('pstr occurs at %d' % idx)
