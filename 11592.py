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

def check_meeting_pos(first, second):
    return first[1] * (second[0] - first[0]) / (first[1] - second[1])


def get_simple_result(D, K, S):
    arr_time = (D - K) / S
    return D / arr_time




if __name__ == '__main__':
    TC = int(input())

    for test_idx in range(1, TC+1):
        D, N = map(int, input().split(" "))
        if N == 1:
            K, S = map(int, input().split(" "))
            result = get_simple_result(D, K, S)
        else:
            first = list(map(int, input().split(" ")))
            second = list(map(int, input().split(" ")))


            if first[0] > second[0]:
                first, second = copy.deepcopy(second), copy.deepcopy(first)

            if first[1] == second[1]:
                result = get_simple_result(D, first[0], first[1])
            else:
                distance = check_meeting_pos(first, second)

                if distance < 0 or distance + first[0] > D:
                    result = get_simple_result(D, first[0], first[1])

                else:
                    min_vel = min(first[1], second[1])
                    arr_time = (second[0] - first[0]) / (first[1] - second[1]) + (D - (distance + first[0])) / min_vel
                    result = D / arr_time



        print("#{} {:7f}".format(test_idx, result))
