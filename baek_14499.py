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

def dice_action(dice_list, action):
    if action == 1:
        return [dice_list[3], dice_list[1], dice_list[0], dice_list[5], dice_list[4], dice_list[2]]
    elif action == 2:
        return [dice_list[2], dice_list[1], dice_list[5], dice_list[0], dice_list[4], dice_list[3]]
    elif action == 3:
        return [dice_list[4], dice_list[0], dice_list[2], dice_list[3], dice_list[5], dice_list[1]]
    elif action == 4:
        return [dice_list[1], dice_list[5], dice_list[2], dice_list[3], dice_list[0], dice_list[4]]



if __name__ == '__main__':
    N, M, init_x, init_y, K = map(int, input().split(" "))

    dice_axis = [init_y, N - init_x - 1]
    dice_list = [0]*6
    map_list = [[0] * N for _ in range(M)]          #### [x][y], [col][row]
    for row in range(N):
        tmp_list = list(map(int, input().split(" ")))
        for col in range(M):
            map_list[col][N - row - 1] = tmp_list[col]


    action_list = list(map(int, input().split(" ")))
    for action in action_list:
        prev_dice_axis = copy.deepcopy(dice_axis)
        if action == 1:
            dice_axis[0] += 1
        elif action == 2:
            dice_axis[0] -= 1
        elif action == 3:
            dice_axis[1] += 1
        elif action == 4:
            dice_axis[1] -= 1
        if dice_axis[0] < 0 or dice_axis[0] >= M or dice_axis[1] < 0 or dice_axis[1] >= N:
            dice_axis = copy.deepcopy(prev_dice_axis)
            continue

        dice_list = dice_action(dice_list, action)
        if map_list[dice_axis[0]][dice_axis[1]] == 0:
            map_list[dice_axis[0]][dice_axis[1]] = dice_list[5]
        else:
            dice_list[5] = map_list[dice_axis[0]][dice_axis[1]]
            map_list[dice_axis[0]][dice_axis[1]] = 0
        print(dice_list[0])





