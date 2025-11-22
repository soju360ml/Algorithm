# Bubble sort
import random

source = [random.randrange(100) for _ in range(100)]

print('Unsorted List'.center(40, '*'))
for i in range(len(source) // 10):
    print(*source[i * 10:i * 10 + 10])

for i in range(len(source) - 1):
    for j in range(len(source) - 1 - i):
        if source[j] > source[j + 1]:
            tmp = source[j]
            source[j] = source[j + 1]
            source[j + 1] = tmp

print('Sorted List'.center(40, '*'))
for i in range(len(source) // 10):
    print(*source[i * 10:i * 10 + 10])