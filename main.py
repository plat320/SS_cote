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

    def one(mat):
        tmp = copy.deepcopy(mat[1])
        mat[1] = copy.deepcopy(mat[2])
        mat[2] = tmp

        return mat

    def four(mat):
        tmp = copy.deepcopy(mat[0])
        mat[0] = copy.deepcopy(mat[3])
        mat[3] = tmp

        return mat

    def find_cord(n, a):
        First_pattern = [1, 2, 4, 3]
        pattern_dict = {}
        pattern_dict[n] = First_pattern
        result = [0, 0]
        a = a - 1

        for idx in range(n):
            tmp_idx = n - 1 - idx

            division = (a // (2 ** (2 * tmp_idx)))
            etc = a % (2 ** (2 * tmp_idx))

            if division == 0:
                pattern_dict[tmp_idx] = one(pattern_dict[tmp_idx + 1])
            elif division == 3:
                pattern_dict[tmp_idx] = four(pattern_dict[tmp_idx + 1])
            else:
                pattern_dict[tmp_idx] = pattern_dict[tmp_idx + 1]

            real_division = pattern_dict[tmp_idx + 1].index(division + 1)

            if real_division == 1:
                result[0] += 2 ** tmp_idx
            elif real_division == 2:
                result[1] += 2 ** tmp_idx
            elif real_division == 3:
                result[0] += 2 ** tmp_idx
                result[1] += 2 ** tmp_idx


            a = copy.deepcopy(etc)

        return result


    def find_result(n, a, b):
        a_cord = find_cord(n, a)
        b_cord = find_cord(n, b)

        return round(10 * (math.sqrt((a_cord[0] - b_cord[0]) ** 2 + (a_cord[1] - b_cord[1]) ** 2)))



    for test_idx in range(1, T+1):
        n, a, b = (map(int, input().split(" ")))
        print("#{} {}".format(test_idx, find_result(n, a, b)))
