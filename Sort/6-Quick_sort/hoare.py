import random as r

data = [r.randrange(1, 1000) for _ in range(2)]

def qsort(data, left, right):
    # Base Case
    if right <= left:
        return
    
    # Partitioning
    i = left
    for j in range(left, right):
        if data[j] <= data[right]:
            data[j], data[i] = data[i], data[j]
            i += 1
    data[i], data[right] = data[right], data[i]
    
    # Recursive Case
    qsort(data, left, i - 1)
    qsort(data, i + 1, right)

qsort(data, 0, len(data) - 1)
print(data)