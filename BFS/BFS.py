# BFS(Breadth First Search) -> 너비 우선 탐색
# 가장 가까운 계층을 최우선적으로 탐색한다
# First in First out -> 큐를 이용한다
# 방향성이 존재한다 -> Directed Graph
# 방향성이 없다(쌍방향) -> Undirected Graph
# Target을 찾는 것이 목표, 찾지 못했다면 해당 노드의 인접리스트를 큐에 등록한다
# 이미 검문한 노드는 기록하여두고 검문을 해야하는지 아닌지 판단할 수 있게 한다

from collections import deque

AdjacencyList = {
    'CAB': ['CAR', 'CAT'],
    'CAR': ['BAR'],
    'CAT': ['BAT', 'MAT'],
    'BAR': ['BAT'],
    'MAT': ['BAT']
}

node = 'CAB'
myQue = deque()
checkedList = {}
myQue.appendleft(node)
findFlag = False

while myQue:
    curNode = myQue.popleft()
    if curNode not in checkedList:
        if curNode == 'BAT':
            findFlag = True
            break
        else:
            myQue += AdjacencyList[curNode]
            checkedList[curNode] = True

if findFlag is True:
    print("BAT found!")