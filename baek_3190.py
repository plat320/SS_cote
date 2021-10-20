import sys
sys.stdin = open("input.txt", "r")

'''
제출시 위는 뺄 것
'''

import math
import copy


def turn_bam_head(dir, turn):
    if turn == "D":
        return [dir[1], -dir[0]]
    if turn == "L":
        return [-dir[1], dir[0]]

if __name__ == '__main__':
    N = int(input())
    K = int(input())
    apple_list = [list(map(int, input().split(" "))) for _ in range(K)]

    L = int(input())
    turn_dict = dict()
    for _ in range(L):
        tmp1, tmp2 = map(str, input().split(" "))
        turn_dict[int(tmp1)] = tmp2

    bam_head_axis = [1, 1]
    bam_head_dir = [0, 1]
    bam_body_list = []

    time = 0

    while True:
        if time in turn_dict.keys():
            bam_head_dir = turn_bam_head(bam_head_dir, turn_dict[time])
        time += 1

        tmp_bam_head_axis = [bam_head_axis[0] + bam_head_dir[0], bam_head_axis[1] + bam_head_dir[1]]

        if tmp_bam_head_axis[0] <= 0 or tmp_bam_head_axis[0] > N or tmp_bam_head_axis[1] <= 0 or tmp_bam_head_axis[1] > N:
            break

        if tmp_bam_head_axis in bam_body_list:
            break

        bam_body_list.append(bam_head_axis)
        if tmp_bam_head_axis not in apple_list:
            bam_body_list.pop(0)
        else:
            apple_list.remove(tmp_bam_head_axis)

        bam_head_axis = copy.deepcopy(tmp_bam_head_axis)

    print(time)