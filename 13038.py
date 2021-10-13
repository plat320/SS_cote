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

def get_left_days(my_list, etc_class):
    result = 100
    for start_idx, val in enumerate(my_list):
        if val == 0:
            continue

        calc_class = 0
        calc_idx = 0
        while True:
            calc_class += my_list[(start_idx + calc_idx) % len(my_list)]
            calc_idx += 1
            if calc_class == etc_class:
                break


        if result > calc_idx:
            result = calc_idx

    return result

if __name__ == '__main__':
    T = int(input())

    for test_idx in range(1, T+1):
        N = int(input())
        my_list = list(map(int, input().split(" ")))

        class_per_week = sum(my_list)

        must_week = N // class_per_week

        etc_class = N % class_per_week
        if etc_class == 0:
            etc_class = class_per_week
            must_week -= 1

        left_days = get_left_days(my_list, etc_class)

        result = must_week * 7 + left_days


        print("#{} {}".format(test_idx, result))
