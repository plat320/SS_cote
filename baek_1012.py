import sys
sys.stdin = open("input.txt", "r")

'''
제출시 위는 뺄 것
'''

import math
import copy

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(M, N, a, b, baechoo_list):
    bug_list = [[a, b]]
    while len(bug_list) != 0:
        for idx in range(4):
            q = bug_list[0][0] + dx[idx]
            w = bug_list[0][1] + dy[idx]
            if 0 <= q < M and 0 <= w < N and baechoo_list[q][w] == 1:
                baechoo_list[q][w] = 0
                bug_list.append([q, w])

        del bug_list[0]

if __name__ == '__main__':
    TC = int(input())
    for test_case in range(1, TC + 1):
        M, N, K = map(int, input().split(" "))

        baechoo_list = [[0] * N for _ in range(M)]
        for _ in range(K):
            a, b = map(int, input().split(" "))
            baechoo_list[a][b] = 1

        cnt = 0
        for x in range(M):
            for y in range(N):
                if baechoo_list[x][y] == 1:
                    bfs(M, N, x, y, baechoo_list)
                    baechoo_list[x][y] = 0
                    cnt += 1

        print(cnt)
