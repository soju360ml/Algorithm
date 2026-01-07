# 힙큐를 리스트로 구현, extract부분 다듬기바람

class HeapQueue:
    def __init__(self, v):
        self.lst = [v]
    def insert(self, v):
        self.lst.append(v)
        idx = len(self.lst) - 1
        pidx = (idx - 1) // 2
        while pidx >= 0 and v > self.lst[pidx]:
            self.lst[idx], self.lst[pidx] = self.lst[pidx], self.lst[idx]
            idx = pidx
            pidx = (idx - 1) // 2
    def extract(self) -> int:
        if len(self.lst) > 0:
            Value = self.lst[0]
        else:
            return None
        if len(self.lst) - 1 > 0:
            self.lst[0] = self.lst.pop()
        else:
            self.lst.pop()
        idx = 0
        cidx = idx * 2 + 1
        while cidx < len(self.lst):
            if cidx + 1 < len(self.lst) and self.lst[cidx + 1] > self.lst[cidx]:
                cidx += 1
            if self.lst[idx] < self.lst[cidx]:
                self.lst[idx], self.lst[cidx] = self.lst[cidx], self.lst[idx]
                idx = cidx
                cidx = idx * 2 + 1
        return Value