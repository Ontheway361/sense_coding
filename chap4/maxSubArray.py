#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2020/07/12
author: relu
"""

from IPython import embed

def maxCross(nums, left, mid, right):

    mleft, l_maxidx = mid, mid
    leftsum, l_maxsum = 0, -float('inf')
    while mleft >= left:
        leftsum += nums[mleft]
        if l_maxsum < leftsum:
            l_maxsum = leftsum
            l_maxidx = mleft
        mleft -= 1

    mright, r_maxidx = mid + 1, mid + 1
    rightsum, r_maxsum = 0, -float('inf')
    while mright <= right:

        rightsum += nums[mright]
        if r_maxsum < rightsum:
            r_maxsum = rightsum
            r_maxidx = mright
        mright += 1
    return (l_maxidx, r_maxidx, int(l_maxsum+r_maxsum))


def findMaxSub(nums, left, right):

    if left == right:
        return (left, left, nums[left])
    else:
        mid = (left + right) // 2
        ll_idx, lr_idx, l_maxsum = findMaxSub(nums, left, mid)
        cl_idx, cr_idx, c_maxsum = maxCross(nums, left, mid, right)
        rl_idx, rr_idx, r_maxsum = findMaxSub(nums, mid + 1, right)
        if l_maxsum >= max(c_maxsum, r_maxsum):
            return (ll_idx, lr_idx, l_maxsum)
        elif r_maxsum >= max(l_maxsum, c_maxsum):
            return (rl_idx, rr_idx, r_maxsum)
        else:
            return (cl_idx, cr_idx, c_maxsum)

def maxSubArray(nums):

    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        lidx, ridx, maxsum = findMaxSub(nums, 0, len(nums)-1)
        print(lidx, ridx, maxsum)
        return maxsum


if __name__ == "__main__":

    # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums = [-1, -1, -2, -2]
    maxsum = maxSubArray(nums)
