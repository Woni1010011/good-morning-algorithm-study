# https://www.acmicpc.net/problem/10026
# dfs 문제

import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(input().rstrip('\n')) for _ in range(n)]
visited = [[False] * n for _ in range(n)]


print(matrix)