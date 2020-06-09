#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2020/06/07
author: relu
"""

from IPython import embed

def dpMakeChange(coinValueList, amnt):

    coinsNum  = [0] * (amnt + 1)
    coinsUsed = [0] * (amnt + 1)
    for cur_amt in range(1, amnt + 1):

        num_coins = cur_amt
        newCoin   = 1
        coin_can_used = [c for c in coinValueList if c <= cur_amt]
        for j in coin_can_used:
            if coinsNum[cur_amt - j] + 1 < num_coins:
                num_coins = coinsNum[cur_amt - j] + 1
                newCoin = j
        coinsNum[cur_amt] = num_coins
        coinsUsed[cur_amt] = newCoin
    return coinsNum[amnt], coinsUsed


def printCoins(coinsUsed, amnt):

	while amnt > 0:
		usecoin = coinsUsed[amnt]
		print(usecoin, end = '、')
		amnt = amnt - usecoin


if __name__ == "__main__":

	amnt = 2
	clist = [1, 2, 5, 10, 25]
	num_coins, details = dpMakeChange(clist, amnt)
	print("找零" + str(amnt) + "美分需要" + str(num_coins) + "个硬币。")
	print("detail :")
	printCoins(details, amnt)
