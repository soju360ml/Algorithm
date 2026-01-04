# 삽입정렬은 순방향일 때 패스하므로 이미 정렬된 경우 O(n)이다
# 또한 데이터의 개수가 적을 때는 O(n)에 가까운 time complexity를 가지므로 timeSort 등에서 분할된 리스트를 정렬할 때 이것과 혼합해서 사용한다

# 삽입정렬에 대한 이해
# 삽입정렬의 삽입이라는 말을 생각해보자
# 리스트를 순차적으로 순회하면서 마주한 데이터가 역방향이면
# 이전 데이터들과 역순회하면서
# 올바른 위치에 삽입하는 정렬이다

import random

source = [random.randrange(100) for _ in range(100)]

print(' Unsorted '.center(50, '-'))
for i in range(len(source) // 10):
    print(*source[i * 10:i * 10 + 10])

for i in range(1, len(source)):
    for j in range(i, -1, -1):
        if source[j] < source[j - 1]:
            v = source[j]
            source[j] = source[j - 1]
            source[j - 1] = v
        else: break

print('Sorted List'.center(50, '*'))
for i in range(len(source) // 10):
    print(*source[i * 10:i * 10 + 10])