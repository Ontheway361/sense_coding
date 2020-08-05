#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2020/08/04
author: relu
"""

class Graph(object):
    def __init__(self, graph):
        self.graph = graph
        self.maxv = float('inf')
        self.n_vertices = self.get_num_vertices()
        self.n_edges = self.get_num_edges()

    def get_num_vertices(self):
        return len(self.graph)

    def get_num_edges(self):
        count = 0
        for i in range(self.n_vertices):
            for j in range(i):
                if self.graph[i][j] > 0 and self.graph[i][j] < self.maxv:
                    count += 1
        return count

    def kruskal(self):
        res = []
        if self.n_vertices <= 0 or self.n_edges < self.n_vertices - 1:
            return res
        edge_list = []
        for i in range(self.n_vertices - 1):
            for j in range(i + 1, self.n_vertices):
                if self.graph[i][j] < self.maxv :
                    edge_list.append([i, j, self.graph[i][j]])
        edge_list.sort(key=lambda a:a[2])
        print(edge_list)
        group = [[i] for i in range(self.n_vertices)]
        for edge in edge_list:
            for i in range(len(group)):
                if edge[0] in group[i]:
                    m = i
                if edge[1] in group[i]:
                    n = i
            if m != n:
                res.append(edge)
                group[m] = group[m] + group[n]
                group[n] = []
        return res

    def prim(self):
        '''
        连通图
        '''
        res = []
        if self.n_vertices <= 0 or self.n_edges < self.n_vertices - 1:
            return res
        res = []
        seleted_node = [0]
        candidate_node = [i for i in range(1, self.n_vertices)]

        while len(candidate_node) > 0:
            begin, end, cur_min = 0, 0, self.maxv
            for i in seleted_node:
                for j in candidate_node:
                    if self.graph[i][j] < cur_min:
                        cur_min = self.graph[i][j]
                        begin = i
                        end = j
            res.append([begin, end, cur_min])
            seleted_node.append(end)
            candidate_node.remove(end)
        return res

max_value = float('inf')
row0 = [0,7,max_value,max_value,max_value,5]
row1 = [7,0,9,max_value,3,max_value]
row2 = [max_value,9,0,6,max_value,max_value]
row3 = [max_value,max_value,6,0,8,10]
row4 = [max_value,3,max_value,8,0,4]
row5 = [5,max_value,max_value,10,4,0]
graph = Graph([row0, row1, row2,row3, row4, row5])
print('邻接矩阵为\n%s' % graph.graph)
print('节点数据为%d，边数为%d\n'%(graph.n_vertices, graph.n_edges))
print('------最小生成树kruskal算法------')
print(graph.kruskal())
print('------最小生成树prim算法')
print(graph.prim())
