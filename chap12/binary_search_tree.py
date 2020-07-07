#!/usr/bin/env python3
#-*- coding:utf-8 -*-
"""
Created on 2020/07/07
author: relu
"""

import numpy as np
from IPython import embed

class binaryTreeNode(object):

    def __init__(self, data, parent = None, left = None, right = None):

        self.data   = data
        self.parent = parent
        self.left   = left
        self.right  = right

class binarySearchTree(object):

    def __init__(self):

        self.root = None
        self.len  = 0

    def _min(self, node = None):

        if node is None:
            node = self.root
        while node.left is not None:
            node = node.left
        return node

    def _max(self, node = None):

        if node is None:
            node = self.root
        while node.right is not None:
            node = node.right
        return node

    def _search(self, data):

        node = self.root
        while (node is not None) and node.data != data:
            if node.data < data:
                node = node.right
            else:
                node = node.left
        if node is not None:
            return node
        else:
            return None

    def _predecessor(self, node):
        '''
        case-1. node.left is not None
        case-2. node.left == None
        '''
        if node.left is not None:
            return self._max(node.left)
        prenode = node.parent
        while prenode is not None and prenode.left == node:
            node = prenode
            prenode = prenode.parent
        return prenode

    def _successor(self, node):

        if node.right is not None:
            return self._min(node.right)
        sucnode = node.parent
        while sucnode is not None and sucnode.right == node:
            node = sucnode
            sucnode = sucnode.parent
        return sucnode

    def _insert(self, node):

        temp, prenode = self.root, None
        while temp is not None:
            prenode = temp
            if temp.data <= node.data:
                temp = temp.right
            else:
                temp = temp.left
        node.parent = prenode
        if prenode is None:
            self.root = node
        elif prenode.data <= node.data:
            prenode.right = node
        else:
            prenode.left = node
        self.len = self.len + 1

    def _up_broadcase(self, dnode, sucnode):
        ''' update the parent-info of sucnode '''
        if dnode.parent is None:
            self.root = sucnode
        elif dnode.parent.left == dnode:
            dnode.parent.left = sucnode
        else:
            dnode.parent.right = sucnode
        if sucnode is not None:
            sucnode.parent = dnode.parent

    def _delete(self, node):

        if node.left is None:
            self._up_broadcase(node, node.right)
        elif node.right is None:
            self._up_broadcase(node, node.left)
        else:
            sucnode = self._min(node.right)
            if sucnode.parent != node:
                self._up_broadcase(sucnode, sucnode.right)
                sucnode.right = node.right
                node.right.parent = sucnode
            self._up_broadcase(node, sucnode)
            sucnode.left = node.left
            node.left.parent = sucnode
        self.len = self.len - 1

    def _build_bst(self, datalist = []):

        for val in datalist:
            temp = binaryTreeNode(data=val)
            self._insert(temp)

    def _inorder_walk(self, node = None):

        if node is not None:
            self._inorder_walk(node.left)
            print(node.data)
            self._inorder_walk(node.right)

    def _preorder_walk(self, node = None):

        if node is not None:
            print(node.data)
            self._preorder_walk(node.left)
            self._preorder_walk(node.right)

    def _postorder_walk(self, node = None):

        if node is not None:
            self._postorder_walk(node.left)
            self._postorder_walk(node.right)
            print(node.data)


if __name__ == "__main__":

    bst = binarySearchTree()
    # datalist = np.random.randint(low=0, high=100, size=10).tolist()
    datalist = [37, 80, 50, 36, 29, 21, 37, 6, 95, 13]
    print(datalist)
    bst._build_bst(datalist)
    bst._inorder_walk(bst.root)
    embed()
