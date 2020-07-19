#!/usr/bin/env python3
#-*- coding:utf-8 -*-
"""
Created on 2020/07/19
author: relu
"""
from IPython import embed

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def showlinkedlist(head):

    walk = head
    while walk:
        print(walk.val)
        walk = walk.next


def list2linkedlist(nums, show = False):

    head = ListNode(nums[0])
    walk = head
    for v in nums[1:]:
        walk.next = ListNode(v)
        walk = walk.next
    walk.next = None
    # print(linkedlist)
    if show:
        showlinkedlist(head)
    return head


def sort_by_pivot(pivot_node, end_node = None):

    walk_node, walk_next = pivot_node.next, None
    left_pivot, right_end = pivot_node, pivot_node
    while walk_node != end_node:

        walk_next = walk_node.next
        if walk_node.val < pivot_node.val:
            walk_node.next = left_pivot
            left_pivot = walk_node
        else:
            right_end.next = walk_node
            right_end = walk_node
        walk_node = walk_next
    right_end.next = end_node
    return left_pivot


def sort_helper(pivot_node, end_node):

    if (pivot_node != end_node) and  (pivot_node.next != end_node):
        left_pivot = sort_by_pivot(pivot_node, end_node)
        # print('left_pivot.val = ', left_pivot.val)
        # if left_pivot.val == -1:
        #     showlinkedlist(pivot_node)
        #     embed()

        sort_helper(left_pivot, pivot_node)
        sort_helper(pivot_node.next, end_node)


def sortList(head):

    new_head, temp = head, head
    while temp:

        if new_head.val > temp.val:
            new_head = temp
        temp = temp.next
    print('new_head.val : %d' % new_head.val)
    sort_helper(head, None)
    return new_head


if __name__ == "__main__":

    # nums = [-1, 5, 3, 4, 0]
    # nums = [4, 2, 1, 3]
    nums = [4, 3, 8, 9, 10, 1, 2]
    head = list2linkedlist(nums)
    new_head = sortList(head)
    showlinkedlist(new_head)
