#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2020/08/05
author: relu
"""

from IPython import embed

def dfs(adjlist, srcidx = 3):
    stack, result = [], []
    stack.append(srcidx)
    result.append(srcidx)
    while len(result) < len(adjlist):

        find_next = False
        for idx, adj in enumerate(adjlist[stack[-1]]):
            if adj and (idx != stack[-1]) and (idx not in result):
                stack.append(idx)
                result.append(idx)
                find_next = True
                break
        if not find_next:
            stack.pop()
    return result


if __name__ == "__main__":

    adjlist = [
        [1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 1],
    ]
    stack = dfs(adjlist, srcidx=0)
    print(stack)
