import sys
import collections
input = sys.stdin.readline

T = int(input())
result = []

for _ in range(T):
    # N 노드 수 M 간선 수
    N, M = map(int, input().split())
    # 인접리스트
    adj = {i: [] for i in range(1, N + 1)}
    # 간선 수
    count = 0
    # 방문노드
    visited = set()
    # 큐
    que = collections.deque()
    for _ in range(M):
        n1, n2 = map(int, input().split())
        adj[n1].append(n2)
        adj[n2].append(n1)
    que.append(list(adj.keys())[0])
    while que:
        vertex = que.popleft()
        if vertex in visited:
            continue
        for i in adj[vertex]:
            que.append(i)
        visited.add(vertex)
        count += 1
    result.append(count - 1)

for i in result:
    print(i)