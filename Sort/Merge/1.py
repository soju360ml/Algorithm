# 병합정렬(MergeSort)를 구현해보자
# 원본을 수정하도록 구현한다
# 재귀함수로 구현

def Merge(requiredList: list, left: int, right: int):
    if left < right:
        center = (left + right) // 2

        Merge(requiredList, left, center)
        Merge(requiredList, center + 1, right)

        # 소스배열의 크기만큼 임시버퍼를 생성한다
        buff = [None] * (right - left + 1)
        i = k = left
        j = p = 0
        
        # 소스배열의 왼쪽파트 전체를 버퍼로 옮긴다
        while i <= center:
            buff[p] = requiredList[i]
            i += 1
            p += 1

        # 임시버퍼와 소스배열 오른쪽파트를 선형비교하여 소스배열에 순차적으로 축적한다
        while i <= right and j < p:
            if requiredList[i] < buff[j]:
                requiredList[k] = requiredList[i]
                i += 1
            else:
                requiredList[k] = buff[j]
                j += 1
            k += 1

        # 버퍼에 남은 잉여원소 모두 원본리스트에 append한다
        # 소스의 왼쪽파트와 오른쪽파트는 이미 정렬된 상태이므로 버퍼의 모든 요소가 소스배열에 들어간 시점이 곧 소스배열의 전체가 정렬된 시점이다
        # 버퍼가 아니라 오른쪽배열의 전체요소가 먼저 소스배열에 축적된 경우 버퍼의 남은 요소들을 소스배열에 단순축적만 하면 소스배열의 전체가 정렬된다
        while j < p:
            requiredList[k] = buff[j]
            k += 1
            j += 1

        # 임시버퍼 해제명시
        del buff

a = [9,7,5,3,1]
b = [2,4,6,8]
c = a + b

Merge(c, 0, 8)
print(c)