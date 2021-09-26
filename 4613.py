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
        color_dict = {}
        for row in range(N):
            ##### color_dict[row] = [W B R]
            color_list = list(input())
            color_dict[row] = [color_list.count("W"), color_list.count("B"), color_list.count("R")]

        min_val = M * N
        for W_end in range(N):
            if W_end == 0: continue
            for B_end in range(W_end, N-1):
                summation_list = [0,0,0]
                for W_row in range(W_end):
                    summation_list[0] += color_dict[W_row][0]
                for B_row in range(W_end, B_end+1):
                    summation_list[1] += color_dict[B_row][1]
                for R_row in range(B_end+1, N):
                    summation_list[2] += color_dict[R_row][2]

                result = N * M - sum(summation_list)
                if min_val > result:
                    min_val = result


        print("#{} {}".format(test_idx, min_val))

