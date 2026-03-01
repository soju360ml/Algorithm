M, m = map(int, input().split())

while m:
    M, m = m, M % m
print(M)