import random

source = [random.randrange(1, 100) for _ in range(300)]

def qsort(source):
    if len(source) <= 1:
        return source
    else:
        pivot = source[-1]
        left = [i for i in source[:-1] if i <= pivot]
        right = [i for i in source[:-1] if i > pivot]
        return qsort(left) + [pivot] + qsort(right)

print(source)
print()
print(qsort(source))