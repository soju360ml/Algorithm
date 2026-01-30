# 다익스트라는 그리디이다. 그리디를 위해 매순간 최소값을 찾기 위해 힙큐(최소우선순위큐) 자료구조를 이용한다
import heapq

# 엔드노드 방문 즉시 모든 노드 거리테이블을 리턴한다
def dijk(start: int, end: int, graph: dict) -> dict:
    # 