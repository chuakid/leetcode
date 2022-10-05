from typing import List


class UFDS:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
        self.size = [1 for _ in range(size)]

    def find(self, x):
        if self.root[x] == x:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def union(self, a, b):
        roota = self.find(a)
        rootb = self.find(b)
        if roota == rootb:
            return
        if self.rank[roota] == self.rank[rootb]:
            self.root[rootb] = roota
            self.size[roota] += self.size[rootb]
            self.rank[roota] += 1
        elif self.rank[roota] < self.rank[rootb]:
            self.root[roota] = self.root[rootb]
            self.size[rootb] += self.size[roota]
        else:
            self.root[rootb] = roota
            self.size[roota] += self.size[rootb]


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restrictedSet = set(restricted)
        ufds = UFDS(n)
        for u, v in edges:
            if u in restrictedSet or v in restrictedSet:
                continue
            ufds.union(u, v)
        return ufds.size[ufds.find(0)]
