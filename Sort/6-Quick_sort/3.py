import random

# source = [random.randrange(1, 1000) for _ in range(1000)]
source = [15, 20, 10]
print(source)

def qsort(data, left, right):
    # Base Case
    if right <= left:
        return
    
    # Partitioning
    leftMarker = left
    rightMarker = right - 1

    while True:
        # 좌마커가 우마커를 추월한 경우 분할완료
        if leftMarker > rightMarker:
            data[leftMarker], data[right] = data[right], data[leftMarker]
            # print('교체완료')
            break
        else:
            # 마커 둘 모두 피벗과 비교조건 성공 시 스왑
            if data[leftMarker] > data[right] and data[rightMarker] <= data[right]:
                data[leftMarker], data[rightMarker] = data[rightMarker], data[leftMarker]
            if data[leftMarker] <= data[right]: leftMarker += 1
            if data[rightMarker] > data[right]: rightMarker -= 1
    
    # Recursive Case
    qsort(data, left, leftMarker - 1)
    qsort(data, leftMarker + 1, right)

qsort(source, 0, len(source) - 1)
print(source)