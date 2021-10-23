import sys
sys.stdin = open("input.txt", "r")

'''
제출시 위는 뺄 것
'''

import math
import copy

def dfs(parent_list, waste):
    parent_list[waste] = -2
    for idx, node in enumerate(parent_list):
        if node == waste:
            dfs(parent_list, idx)


if __name__ == '__main__':
    N = int(input())

    parent_list = list(map(int, input().split(" ")))
    waste = int(input())

    dfs(parent_list, waste)

    cnt = 0
    for idx, node in enumerate(parent_list):
        if node != -2 and idx not in parent_list:
           cnt += 1

    print(cnt)