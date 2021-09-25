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

def find_all_idx(my_list, value):
    target_list = []
    for idx, val in enumerate(my_list):
        if val == value:
            target_list.append(idx)

    return target_list

def find_max_idx(my_list):
    max_idx_list = []
    tmp_list = copy.deepcopy(my_list)

    while True:
        max_value = max(tmp_list)
        # subtarget_list = find_all_idx(my_list, max_value)
        # max_idx = subtarget_list[-1]
        max_idx = len(my_list) - list(reversed(my_list)).index(max_value) - 1
        max_idx_list.append(max_idx)
        tmp_list = my_list[max_idx+1:]

        #### break condition
        if max_idx == len(my_list) - 1:
            break

    return max_idx_list

def make_value_list(my_list, idx_list):
    target_list = []
    tmp_val = 0
    result = 0
    for val in idx_list:
        result += my_list[val] * (val - tmp_val + 1)
        # for i in range(val - tmp_val + 1):
        #     target_list.append(my_list[val])
        #
        tmp_val = val +1

    return result
    # return target_list



if __name__ == '__main__':

    # result = random_List(1000000)
    # print(result)
    # max_idx_list = find_max_idx(result)
    # value_list = make_value_list(result, max_idx_list)
    # print(value_list)
    # a = value_list - sum(result)
    # print("{}".format(a))
    T = int(input())

    for idx in range(1, T + 1):
        len_list = int(input())
        my_list = list(map(int, input().split(" ")))

        max_idx_list = find_max_idx(my_list)
        value_list = make_value_list(my_list, max_idx_list)

        result = value_list - sum(my_list)
        # result = sum(value_list) - sum(my_list)





        print("#{} {}".format(idx, result))