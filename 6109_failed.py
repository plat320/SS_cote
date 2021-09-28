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


def find_result(my_dict, N):
    result_dict = [[0] * N for _ in range(N)]
    for row in range(N):
        blank_count = 0
        ref_num = 0
        for col in range(N):
            check_num = my_dict[row][col]
            if ref_num == 0:
                ref_num = check_num
                if col == N - 1:
                    result_dict[row][blank_count] = check_num
            else:
                if check_num == 0:
                    if col == N-1:
                        result_dict[row][blank_count] = ref_num
                        print(ref_num)
                elif ref_num == check_num:
                    result_dict[row][blank_count] = ref_num * 2
                    blank_count +=1
                    ref_num = 0
                else:
                    result_dict[row][blank_count] = ref_num
                    blank_count += 1
                    ref_num = check_num
                if col == N - 1:
                    result_dict[row][blank_count] = check_num


    # for row in range(N):
    #     check_num = 0
    #     for col in range(N):
    #         last_dir_col = col - 1
    #
    #         cur_num = my_dict[row][col]
    #
    #         if check_num == 0:
    #             if cur_num == 0:
    #                 continue
    #             else:
    #                 check_num = cur_num
    #                 if col == N - 1:
    #                     result_dict[row][last_dir_col] = cur_num
    #
    #         else:
    #             if cur_num == 0:
    #                 if col == N - 1:
    #                     result_dict[row][col] = check_num
    #             elif cur_num == check_num:
    #                 result_dict[row][last_dir_col] = 2* cur_num
    #                 check_num = 0
    #             elif cur_num != check_num:
    #                 result_dict[row][last_dir_col] = check_num
    #                 check_num = cur_num
    #                 if col == N - 1:
    #                     result_dict[row][col] = cur_num
    #
    # final_list = [[0]*N for _ in range(N)]
    # for row in range(N):
    #     count_zero = 0
    #     count_non_zero = 0
    #     for col in range(N):
    #         if result_dict[row][col] == 0:
    #             continue
    #         else:
    #             final_list[row][count_non_zero] = result_dict[row][col]
    #             count_non_zero += 1
    #     for idx in range(count_zero):
    #         final_list[row][count_non_zero + idx] = 0

    print(result_dict)
    return result_dict

def reflect(my_list, N):
    tmp_list = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            tmp_list[row][col] = my_list[col][row]

    return tmp_list

def lr_shift(my_list, N):
    tmp_list = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            tmp_list[row][col] = my_list[row][N-1-col]

    return tmp_list




if __name__ == '__main__':
    T = int(input())

    for test_idx in range(1, T+1):
        N, B = map(str, input().split(" "))
        N = int(N)
        if N == 1:
            print("#{}".format(test_idx))
            print("{}".format(int(input())))
        else:
            tile_list = [[0] * N for _ in range(N)]
            for idx in range(N):
                tile_list[idx] = list(map(int, input().split(" ")))


            if B == "right":
                tile_list = lr_shift(tile_list, N)
            elif B == "up":
                tile_list = reflect(tile_list, N)
            elif B == "down":
                tile_list = lr_shift(reflect(tile_list, N), N)

            result_list = find_result(tile_list, N)

            if B == "right":
                result_list = lr_shift(result_list, N)
            elif B == "up":
                result_list = reflect(result_list, N)
            elif B == "down":
                result_list = reflect(lr_shift(result_list, N), N)


            print("#{}".format(test_idx))

            for row in range(N):
                for col in range(N):
                    if col != N-1:
                        print(result_list[row][col], end = " ")
                    elif col == N-1:
                        print(result_list[row][col], end = "")
                print()