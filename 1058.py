import sys
sys.stdin = open("input.txt", "r")

'''
제출시 위는 뺄 것
'''

import math
import copy



if __name__ == '__main__':
    N = int(input())

    friend_list = []
    for idx in range(N):
        friend_list.append(list(input()))

    max = 1

    for idx in range(N):
        idx_friend = []
        second_friend = []
        for p_idx in range(N):
            if friend_list[idx][p_idx] == 'Y':
                idx_friend.append(p_idx)

        for first_friend in idx_friend:
            for p_idx in range(N):
                if friend_list[first_friend][p_idx] == 'Y':
                    second_friend.append(p_idx)

        idx_friend.extend(second_friend)
        idx_friend = list(set(idx_friend))

        if len(idx_friend) > max:
            max = len(idx_friend)

    print(max - 1)
