import sys
sys.stdin = open("input.txt", "r")

'''
제출시 위는 뺄 것
'''

import math
import copy



if __name__ == '__main__':
    N, L, R = map(int, input().split(" "))

    map_list = [0] * N
    for row in range(N):
        map_list[row] = list(map(int, input().split(" ")))

    day = -1
    while True:
        break_flag = True
        day += 1


        Union_dict = dict()
        Union_num = 0
        for row in range(N):
            for col in range(N):
                try:            #### check right
                    val = abs(map_list[row][col] - map_list[row][col + 1])
                    if L <= val and R >= val:
                        break_flag = False
                        local_break = False
                        for check_list in Union_dict.items():
                            if [row, col] in check_list[1]:


                                local_break = True
                                Union_dict[check_list[0]].append([row, col + 1])
                                Union_dict[check_list[0]] = list(dict.fromkeys(Union_dict[check_list[0]]))
                                save_Union_num = check_list[0]
                                break


                        for check_list in Union_dict.items():
                            if [row, col + 1] in check_list[1]:


                                if local_break:
                                    if save_Union_num != check_list[0]:
                                        for val in Union_dict[save_Union_num]:
                                            Union_dict[save_Union_num].append(val)
                                        Union_dict.pop(check_list[0])
                                        break

                                else:
                                    local_break = True
                                    Union_dict[check_list[0]].append([row, col])
                                break

                        #### if do not break
                        if not local_break:
                            Union_dict[Union_num] = [[row, col], [row, col + 1]]
                            Union_num += 1
                except:
                    pass

                try:            #### check below
                    val = abs(map_list[row][col] - map_list[row + 1][col])
                    if L <= val and R >= val:
                        break_flag = False
                        local_break = False
                        for check_list in Union_dict.items():
                            if [row, col] in check_list[1]:


                                Union_dict[check_list[0]].append([row + 1, col])
                                local_break = True
                                save_Union_num = check_list[0]
                                break

                        for check_list in Union_dict.items():
                            if [row + 1, col] in check_list[1]:


                                if local_break:
                                    if save_Union_num != check_list[0]:
                                        for val in Union_dict[save_Union_num]:
                                            Union_dict[save_Union_num].append(val)
                                        Union_dict.pop(check_list[0])
                                        break

                                else:
                                    Union_dict[check_list[0]].append([row, col])
                                    local_break = True


                                break


                        #### if do not break
                        if not local_break:
                            Union_dict[Union_num] = [[row, col], [row + 1, col]]
                            Union_num += 1
                except:
                    pass

        if break_flag:
            break

        for key, val in Union_dict.items():
            tmp_list = []
            for value in val:
                if value not in tmp_list:
                    tmp_list.append(value)
            Union_dict[key] = tmp_list

        for key, val in Union_dict.items():
            summation = 0
            for country in val:
                summation += map_list[country[0]][country[1]]
            for country in val:
                map_list[country[0]][country[1]] = summation // len(val)


    print(day)




