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
        N = int(input())
        price_list = sorted(list(map(int, input().split(" "))))[::-1]           # 큰 순서대로 정렬

        last_idx = (N - 1) // 3 + 1
        last_idx_num = (N - 1) % 3
        result = 0
        for idx in range(last_idx):
            if idx == last_idx - 1:
                if last_idx_num == 2:
                    result += sum(price_list[3 * idx: 3 * idx + 2])
                else:
                    result += sum(price_list[3 * idx: 3 * idx + last_idx_num+1])
            else:
                result += sum(price_list[3 * idx: 3 * idx + 2])


        print("#{} {}".format(test_idx, result))