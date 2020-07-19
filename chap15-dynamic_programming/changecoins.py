#!/usr/bin/env python3
#-*- coding:utf-8 -*-
"""
Created on 2020/06/08
author: relu
"""

def changeCoins(coinslist = [], amt = 0):
    ''' change amt dollors with the least number of coins '''

    if amt < 2:
        return amt
    coins_num_at_amt = [0] * (amt + 1)
    change_amt_with_coin = [0] * (amt + 1)
    for cur_amt in range(1, amt + 1):

        max_num_coins = cur_amt
        choice_coin = 1
        for coin in [val for val in coinslist if val <= cur_amt]:

            if coins_num_at_amt[cur_amt - coin] + 1 < max_num_coins:
                max_num_coins = coins_num_at_amt[cur_amt - coin] + 1
                choice_coin = coin
        coins_num_at_amt[cur_amt] = max_num_coins
        change_amt_with_coin[cur_amt] = choice_coin
    return coins_num_at_amt[amt], change_amt_with_coin


def printSolution(change_amt_with_coin = [], amt = 0):
    ''' show the solution '''

    solution = []
    while amt > 0:
        solution.append(change_amt_with_coin[amt])
        amt -= change_amt_with_coin[amt]
    solution.sort()
    print('solution : ', solution)


if __name__ == '__main__':

    amt = 111
    coinslist = [1, 2, 5, 10]
    num_coins, used_coins_list = changeCoins(coinslist, amt)
    print('change %2d dollors, must use at least %d coins' % (amt, num_coins))
    printSolution(used_coins_list, amt)
