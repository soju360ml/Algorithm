# 병합정렬(MergeSort)를 구현해보자
# 원본을 수정하도록 구현한다

def Merge(requiredList: list, left: int, right: int):
    if left < right:
        center = (left + right) // 2

        Merge(requiredList, left, center)
        Merge(requiredList, center + 1, right)

        # 병합구간
        buff = [None] * (right - left + 1)
        i = k = left
        j = p = 0
        
        # 왼쪽리스트 버퍼로 옮기기
        while i <= center:
            buff[p] = requiredList[i]
            i += 1
            p += 1

        # 오른쪽 리스트와 버퍼 비교하여 원본 리스트로 옮기기
        while i <= right and j < p:
            if requiredList[i] < buff[j]:
                requiredList[k] = requiredList[i]
                i += 1
            else:
                requiredList[k] = buff[j]
                j += 1
            k += 1

        # 버퍼에 남은 원소 모두 원본리스트에 append한다
        while j < p:
            requiredList[k] = buff[j]
            k += 1
            j += 1

        # 메모리 해제 명시
        del buff

a = [9,7,5,3,1]
b = [2,4,6,8]
c = a + b

Merge(c, 0, 8)
print(c)