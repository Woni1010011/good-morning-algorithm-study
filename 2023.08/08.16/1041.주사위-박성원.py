# https://www.acmicpc.net/problem/1041
# 주사위가 쌓인다는게 어떻게 쌓이는지 그림이 안그려짐.


import sys
input = sys.stdin.readline

n = int(input())
dice = list(map(int, input().split()))

# 전체합 - 최대값 = 최대값을 제외한 최솟값의 합
if n == 1 :
    print(sum(dice) - max(dice))
else :
    sum_list = [min(dice[0], dice[5]), min(dice[1], dice[4]), min(dice[2], dice[3])]
    sum_list.sort()

    layer1 = (n-2)*(n-2) + (n-1)*(n-2)*4
    layer2 = (n-2)*4 + (n-1)*4
    layer3 = 4

    ans = layer1*sum_list[0] + layer2*sum(sum_list[:2]) + layer3*sum(sum_list)

print(ans)

        
