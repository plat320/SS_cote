import sys

sys.stdin = open("input.txt", "r")
'''
제출시 위는 뺄 것
'''



if __name__ == '__main__':

    T = int(input())

    for idx in range(1, T + 1):
        my_list = list(map(int, input().split(" ")))
        print("#{} {}".format(idx, round(sum(my_list) / len(my_list))))