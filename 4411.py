import sys
import random

def random_List(size):
    result = []

    for v in range(size):
        result.append(random.randint(0, 5000))

    return result

sys.stdin = open("input.txt", "r")

'''
제출시 위는 뺄 것
'''

import math
import copy

if __name__ == '__main__':
    T = int(input())

    for test_idx in range(1, T+1):
        N, K = map(int, input().split(" "))
        result = 1
        for idx in range(1, N):
            result = (result + K) % (idx + 1) + 1
        print("#{} {}".format(test_idx, result))
