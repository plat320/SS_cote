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

import copy
import math


if __name__ == '__main__':
    T = int(input())

    for test_idx in range(1, T+1):
        N, M = map(int, input().split(" "))
        #### 무조건 M이 크거나 같게
        if N > M:
            tmp = N
            N = copy.deepcopy(M)
            M = copy.deepcopy(tmp)


        first_pattern_list = [1 if (idx % 4 < 2) else 0 for idx in range(M)]
        first = sum(first_pattern_list)
        second_pattern_list = [1 if (idx % 4 > 1) else 0 for idx in range(M)]
        second = sum(second_pattern_list)

        result = 0
        for idx in range(N):
            if idx % 4 < 2:
                result += first
            else:
                result += second


        print("#{} {}".format(test_idx, result))
