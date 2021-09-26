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

def find_elavate(A, my_dict):
    result = 0

    for idx in range(12):
        tmp_val = A % (10 ** (idx + 1)) // (10 ** idx)
        if tmp_val > 4:
            result += (10 ** idx) + my_dict[idx] * (tmp_val - 1)
        else:
            result += my_dict[idx] * tmp_val

    return A - result

if __name__ == '__main__':
    T = int(input())

    including4_dict = {}
    including4_dict[0] = 0
    including4_dict[1] = 1
    for idx in range(2, 13):
        including4_dict[idx] = including4_dict[idx - 1] * 9 + 10 ** (idx - 1)


    for test_idx in range(1, T+1):
        A, B = map(int, input().split(" "))

        a_elavate = find_elavate(abs(A), including4_dict)
        b_elavate = find_elavate(abs(B), including4_dict)

        if A > 0:
            if B > 0:
                result = b_elavate - a_elavate

        if A < 0:
            if B > 0:
                result = b_elavate + a_elavate - 1

            else:
                result = a_elavate - b_elavate




        print("#{} {}".format(test_idx, result))

