#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2020/08/05
author: relu
"""

from IPython import embed

def bfs(adjlist, srcidx = 3):
    queue = []
    search_idx = 0
    queue.append(srcidx)
    while len(queue) < len(adjlist):
        node_idx = queue[search_idx]
        for idx, adj in enumerate(adjlist[node_idx]):
            if adj and (idx != node_idx) and (idx not in queue):
                queue.append(idx)
        search_idx += 1
    return queue



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
    queue = bfs(adjlist, srcidx=6)
    print(queue)
