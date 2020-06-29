#!/usr/bin/env python3
#-*- coding:utf-8 -*-
"""
Created on 2020/06/29
author: relu
"""

# https://www.bilibili.com/video/BV1hW411a7ys/?spm_id_from=333.788.videocard.0
from IPython import embed

def prefix_table(pstr = ''):

    prefix = [0] * len(pstr)
    i, sublen = 1, 0
    while i < len(pstr):
        if pstr[i] == pstr[sublen]:
            sublen += 1
            prefix[i] = sublen
            i += 1
        else:
            if sublen > 0:
                sublen = prefix[sublen-1] # why ? ? ?
            else:
                prefix[i] = 0
                i += 1
    return prefix


if __name__ == "__main__":

    tstr = 'ababcabaa'
    func  = prefix_table(tstr)
    print(func)
