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

    for test_idx in range(1, T + 1):
        N, K = map(int, input().split(" "))
        my_list = list(input())[::-1]
        my_list = [1 if val == "B" else -1 for val in my_list]

        summation = 0
        prev_val = 0
        result = 0
        for idx, val in enumerate(my_list):
            summation = 0 if summation + val < 0 else summation + val

            if summation == K + 1:
                summation = K - 1
                my_list[idx] = -1
                result += 2 ** (N - idx)

        print("#{} {}".format(test_idx, result % 998244353))






        # break_flag = False
        #
        # while not break_flag:
        #     right_K_idx = find_K_idx(my_list, K, default_idx)
        #
        #     prev_val = 0
        #     if right_K_idx == len(my_list) - 1:
        #         break_flag = True
        #     for check_idx in range(right_K_idx + 1, len(my_list)):
        #         if my_list[check_idx] == 1 and prev_val != -1:          #### 1 후 1이면 안됨
        #             my_list[check_idx] = -1
        #             idx_list.append(check_idx)
        #             if K == 1:
        #                 default_idx = check_idx
        #                 break
        #         elif my_list[check_idx] == -1:
        #             if prev_val == -1:                                  #### -1이 두 번 나옴
        #                 default_idx = check_idx
        #                 break
        #         prev_val = my_list[check_idx]
        #         if check_idx == len(my_list) - 1:
        #             break_flag = True

