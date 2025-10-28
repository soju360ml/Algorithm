list_1 = [1, 2, 3, 4, 5]
target = 5


def binarySearch(source, target):
    left = 0
    right = len(list_1) - 1
    while left <= right:
        center = (left + right) // 2
        
        if target == source[center]:
            return True
        elif target < source[center]:
            right = center - 1
        elif target > source[center]:
            left = center + 1
        else:
            return False

print(binarySearch(list_1, target))