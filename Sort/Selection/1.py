import random

source = [random.randrange(100) for _ in range(100)]

print(' Unsorted '.center(50, '-'))
for i in range(len(source) // 10):
    print(*source[i * 10:i * 10 + 10])

for i in range(len(source) - 1):
    tmp = source[i]
    tmpI = i
    for j in range(len(source) - 1 - i):
        if tmp > source[i + 1 + j]:
            tmp = source[i + 1 + j]
            tmpI = i + 1 + j
    source[tmpI] = source[i]
    source[i] = tmp

print(' sorted '.center(50, '-'))
for i in range(len(source) // 10):
    print(*source[i * 10:i * 10 + 10])