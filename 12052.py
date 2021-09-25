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


#### 처음부터 list로 변경해놓고 시작하면 훨씬 편하다.. 굳이 find를 사용할 필요 없음

import copy

def check_result(my_list, row):
    result = "YES"
    for idx in range(row):
        while True:
            tmp1_idx = my_list[idx].find("#")
            tmp2_idx = my_list[idx].find("##")
            if tmp1_idx == -1:
                break
            elif tmp1_idx != tmp2_idx:
                result = "NO"
                break
            else:
                try:
                    tmp = my_list[idx+1][tmp1_idx:tmp1_idx+2]
                    if tmp == "##":
                        my_list[idx] = my_list[idx].replace("##", "..", 1)
                        my_list[idx+1] = list(my_list[idx+1])
                        my_list[idx+1][tmp1_idx] = "."
                        my_list[idx+1][tmp1_idx+1] = "."
                        my_list[idx+1] = "".join(my_list[idx+1])
                    else:
                        result = "NO"
                        break
                except:
                    result = "NO"
                    break

    return result


if __name__ == '__main__':
    T = int(input())

    for test_idx in range(1, T+1):
        my_list = []
        row, col = map(int, input().split(" "))
        for _ in range(row):
            my_list.append(input())
        result = check_result(my_list, row)


        print("#{} {}".format(test_idx, result))
