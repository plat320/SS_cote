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

    keypad_dict = {}
    for char in "abc":
        keypad_dict[char] = 2
    for char in "def":
        keypad_dict[char] = 3
    for char in "ghi":
        keypad_dict[char] = 4
    for char in "jkl":
        keypad_dict[char] = 5
    for char in "mno":
        keypad_dict[char] = 6
    for char in "pqrs":
        keypad_dict[char] = 7
    for char in "tuv":
        keypad_dict[char] = 8
    for char in "wxyz":
        keypad_dict[char] = 9
    for test_idx in range(1, T+1):
        S, N = map(int, input().split(" "))
        words = list(map(str, input().split(" ")))
        result = 0
        for idx in range(N):
            save_result = 0
            for char_idx, char in enumerate(words[idx]):
                save_result = save_result * 10 + keypad_dict[char]
            if save_result == S:
                result += 1



        print("#{} {}".format(test_idx, result))
