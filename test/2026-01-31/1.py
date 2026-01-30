def counting_sort(arr):
    #최대값 추출
    max_val = max(arr)

    #카운트배열 초기화
    count_arr = [0] * (max_val + 1)

    #원본배열 요소의 개수 세기
    for value in arr:
        count_arr[value] += 1

    #카운트배열의 값을 누적합으로 변환
    for idx in range(1, len(count_arr)):
        count_arr[idx] += count_arr[idx - 1]

    #결과배열 초기화
    output_arr = [0] * len(arr)

    #결과배열 값 배정
    i = len(arr) - 1
    while i >= 0:
        output_arr[count_arr[arr[i]] - 1] = arr[i]
        count_arr[arr[i]] -= 1
        i -= 1

    return output_arr

# 예시
arr = [4, 2, 2, 8, 3, 3, 1]
sortedArr = counting_sort(arr)
print(sortedArr)