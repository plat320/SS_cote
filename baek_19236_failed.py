import sys
sys.stdin = open("input.txt", "r")

'''
제출시 위는 뺄 것
'''

import math
import copy

def fish_moving(num_list, fish_dict):
    for fish_idx in range(1, 17):
        try:
            dir, prev_pose = fish_dict[fish_idx][0], fish_dict[fish_idx][1]
        except:
            continue

        first_dir = copy.deepcopy(dir)
        while True:
            pose = [dir_mapping[dir][0] + prev_pose[0], dir_mapping[dir][1] + prev_pose[1]]
            if not check_pose(pose):              # 경계 out
                dir += 1
                dir = 1 if dir == 9 else dir
            elif pose[0] == fish_dict[0][1][0] and pose[1] == fish_dict[0][1][1]:       # 상어랑 확인
                dir += 1
                dir = 1 if dir == 9 else dir
            elif not num_list[pose[0]][pose[1]]:
                dir += 1
                dir = 1 if dir == 9 else dir
            else:                                                                       # 물고기 이동 가능 ㅠ
                check_fish_num = num_list[pose[0]][pose[1]]
                if check_fish_num != 0:
                    fish_dict[check_fish_num] = [fish_dict[check_fish_num][0], prev_pose]   # 이전에 있던 물고기 pose 변경
                    num_list[prev_pose[0]][prev_pose[1]] = check_fish_num
                else:
                    num_list[prev_pose[0]][prev_pose[1]] = 0

                fish_dict[fish_idx] = [dir, pose]                                   # 물고기 이동!
                num_list[pose[0]][pose[1]] = fish_idx
                break

            if first_dir == dir:
                break

    return num_list, fish_dict


def shark_ate(num_list, fish_dict):
    axis = fish_dict[0][1]                      # shark pose

    fish_num = num_list[axis[0]][axis[1]]       # which num of fish
    fish_dict[0][0] = fish_dict[fish_num][0]    # update shark dir
    fish_dict.pop(fish_num)                     # update fish info in fish_dict
    num_list[axis[0]][axis[1]] = 0              # update num_list

    return fish_num, num_list, fish_dict

def check_pose(pose):
    if pose[0] < 0 or pose[1] < 0 or pose[0] > 3 or pose[1] > 3:
        return False
    else:
        return True

def find_result(result, num_list, fish_dict):
    global maxv
    current_num_list = copy.deepcopy(num_list)
    current_fish_dict = copy.deepcopy(fish_dict)
    mov_num_list, mov_fish_dict = fish_moving(current_num_list, current_fish_dict)

    shark_pose = mov_fish_dict[0][1]
    shark_dir = dir_mapping[mov_fish_dict[0][0]]

    move1 = [shark_pose[0] + shark_dir[0], shark_pose[1] + shark_dir[1]]
    move2 = [shark_pose[0] + 2 * shark_dir[0], shark_pose[1] + 2 * shark_dir[1]]
    move3 = [shark_pose[0] + 3 * shark_dir[0], shark_pose[1] + 3 * shark_dir[1]]

    if check_pose(move1) and mov_num_list[move1[0]][move1[1]] != 0:
        final_fish_dict = copy.deepcopy(mov_fish_dict)
        final_num_list = copy.deepcopy(mov_num_list)
        final_fish_dict[0][1] = move1
        local_result, final_num_list, final_fish_dict = shark_ate(final_num_list, final_fish_dict)
        find_result(result + local_result, final_num_list, final_fish_dict)

    if check_pose(move2) and mov_num_list[move2[0]][move2[1]] != 0:
        final_fish_dict = copy.deepcopy(mov_fish_dict)
        final_num_list = copy.deepcopy(mov_num_list)
        final_fish_dict[0][1] = move2
        local_result, final_num_list, final_fish_dict = shark_ate(final_num_list, final_fish_dict)
        find_result(result + local_result, final_num_list, final_fish_dict)

    if check_pose(move3) and mov_num_list[move3[0]][move3[1]] != 0:
        final_fish_dict = copy.deepcopy(mov_fish_dict)
        final_num_list = copy.deepcopy(mov_num_list)
        final_fish_dict[0][1] = move3
        local_result, final_num_list, final_fish_dict = shark_ate(final_num_list, final_fish_dict)
        find_result(result + local_result, final_num_list, final_fish_dict)

    if not (check_pose(move1) and mov_num_list[move1[0]][move1[1]] != 0) and not (check_pose(move2) and mov_num_list[move2[0]][move2[1]] != 0) and not (check_pose(move3) and mov_num_list[move3[0]][move3[1]] != 0):
        maxv = max(maxv, result)
        return




dir_mapping = [[], [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]    # 1 ~ 8 -> 반시계방향


if __name__ == '__main__':
    maxv = 0
    num_list = []
    dir_list = []

    fish_dict = dict()
    for row in range(4):
        tmp_list = list(map(int, input().split(" ")))
        num_list.append(tmp_list[0::2])
        for col, (a, b) in enumerate(zip(tmp_list[0::2], tmp_list[1::2])):
            fish_dict[a] = [b, [row, col]]


    fish_dict[0] = [0, [0, 0]]
    init_result, num_list, fish_dict = shark_ate(num_list, fish_dict)

    find_result(init_result, num_list, fish_dict)

    print(maxv)