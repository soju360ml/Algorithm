import random

source = [random.randrange(1, 1000) for _ in range(1000)]
# source = [20, 30, 10]

def qsort(source, left, right, pivot):
    pValue = source[pivot]
    init = left
    while left < pivot and right >= 0:
        if source[left] > pValue and source[right] <= pValue:
            tmp = source[left]
            source[left] = source[right]
            source[right] = tmp
            left += 1
            right -= 1
        if source[left] <= pValue:
            left += 1
        if source[right] > pValue:
            right -= 1
        # left가 right를 넘어선 순간 pivot을 바꿔야한다
        if left > right:
            tmp = source[left]
            source[left] = source[pivot]
            source[pivot] = tmp
            qsort(source, init, left - 2, left - 1)
            qsort(source, left + 1, pivot - 1, pivot)
            return

qsort(source, 0, len(source) - 2, len(source) - 1)
print(source)