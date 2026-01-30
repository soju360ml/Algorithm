from itertools import accumulate
from itertools import islice

# 1번째 방법
source = [i for i in range(1, 11)]
prefixSum = []
total = 0
for i in source:
    total += i
    prefixSum.append(total)
print(prefixSum)

# 2번째 방법 모듈 이용
print(list(accumulate(source)))

# 3번째 방법; 1번째 방법과 비슷하지만 total 변수를 사용하지 않고 prefixSum의 요소를 추가할 때 이전 인덱스의 값을 참조하여 추가한다
prefixSum = []
prefixSum.append(source[0])
for i in range(1, len(source)):
    prefixSum.append(prefixSum[i - 1] + source[i])
print(prefixSum)