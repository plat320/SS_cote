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
        print("#{}".format(test_idx), end=" ")
        N = int(input())
        my_dict = {}
        for idx in range(2, N+1):           # 2~N
            my_dict[idx] = list(map(int, input().split(" ")))

        M = int(input())
        X_list = list(map(int, input().split(" ")))
        for X_input in X_list:
            function_dict = {}
            function_dict[0] = 1
            function_dict[1] = X_input
            for N_idx in range(2, N+1):
                if my_dict[N_idx][0] == 1:
                    function_dict[N_idx] = function_dict[my_dict[N_idx][1]] + function_dict[my_dict[N_idx][2]]
                elif my_dict[N_idx][0] == 2:
                    function_dict[N_idx] = my_dict[N_idx][1] * function_dict[my_dict[N_idx][2]]
                elif my_dict[N_idx][0] == 3:
                    function_dict[N_idx] = function_dict[my_dict[N_idx][1]] * function_dict[my_dict[N_idx][2]]

            print("{}".format(function_dict[N] % 998244353), end=" ")


