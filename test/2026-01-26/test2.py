import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))

sum_arr = []
temp = 0
for a in arr:
    temp += a
    sum_arr.append(temp)

for _ in range(M):
    i, j = map(int, input().split())
    print(sum_arr[j] - sum_arr[i-1])
