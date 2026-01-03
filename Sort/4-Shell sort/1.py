# 셸 정렬 1 4 10 23 57(Marcin Ciura's gap sequence) 여기서는 10까지만 이용
# using loop

import random

source_length = 100 # 요소의 개수
source = [int(random.randrange(1000)) for _ in range(source_length)]
seq = [1, 4]

print(source)
print()

for gap in reversed(seq): # 시퀀스의 요소를 역순으로 꺼낸다 10 > 4 > 1 등
    print(f'<현재 gap: {gap}>\n')
    for 단위인덱스 in range(gap):
        print(f'현재 단위인덱스: {단위인덱스}')
        전진인덱스 = 단위인덱스 + gap # 초기전진인덱스
        # mod 합동 그룹끼리 insertion하는 단계
        while 전진인덱스 < source_length:
            for 왼쪽요소들의인덱스 in range(전진인덱스, -1, -gap):
                print(f'현재 왼쪽요소들의인덱스: {왼쪽요소들의인덱스}')
                if 왼쪽요소들의인덱스 - gap >= 0 and source[왼쪽요소들의인덱스 - gap]  > source[왼쪽요소들의인덱스]:
                    print('스와핑실행')
                    tmp = source[왼쪽요소들의인덱스 - gap]
                    source[왼쪽요소들의인덱스 - gap] = source[왼쪽요소들의인덱스]
                    source[왼쪽요소들의인덱스] = tmp
                else:
                    break
            전진인덱스 += gap

print(source)