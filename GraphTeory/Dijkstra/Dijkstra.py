# 현재까지 발견한 경로 중 최소비용의 경로를 최우선 탐색한다
# 이미 방문한 노드는 재방문하지 않는다 -> 이미 방문한 노드 재방문이 가능하다면 1번에 의해 무한루프가 된다
# BFS와는 다르게 큐를 사용하지 않는다 -> 매 사이클마다 최소비용의 노드를 찾아서 반복하기 때문

# 현재까지 발견한 경로들 중 최소가격을 가지는 노드를 방문한다
def nextNode(visited, costs):
    leastCost = float('inf')
    node = None

    for i in costs:
        if i not in visited and costs[i] < leastCost:
            leastCost = costs[i]
            node = i
    return node

def Dijkstra(start, end, adjacencyList):
    visited = set()
    costs = {}
    parent = {}

    # 모든 도달 가능한 노드의 비용을 inf로 init한다
    for i in adjacencyList:
        for j in adjacencyList[i]:
            costs[j] = float('inf')

    curNode = start # 현재 탐색할 노드를 start로 시작한다
    costs[start] = 0    # 시작 노드는 비용이 0이다

    while curNode:
        for i in adjacencyList[curNode]:
            tmpCost = costs[curNode] + adjacencyList[curNode][i]
            # 경로비용테이블은 이미 inf로 있으니 최소비용으로 갱신만 시키면 된다
            if tmpCost < costs[i]:
                costs[i] = tmpCost
                parent[i] = curNode
        visited.add(curNode)
        curNode = nextNode(visited, costs)
    
    return costs[end]