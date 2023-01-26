import heapq
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # make adj list
        a = [[] for _ in range(n)]
        for s, d, dist in flights:
            a[s].append((d, dist))
        # dijkstra
        pq = []
        heapq.heappush(pq ,(0, 0, src))
        visited = [-1 for _ in range(n)]
        while pq:
            distance,stops,city = heapq.heappop(pq)
            if stops <= k + 1 and city == dst:
                return distance
            if visited[city] != -1 and visited[city] < stops:
                continue
            visited[city] = stops
            for neighbour, distance_to_neighbour in a[city]:
                dist_through_city = distance + distance_to_neighbour
                heapq.heappush(pq, (dist_through_city, stops + 1, neighbour))
        return -1
print(Solution().findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
, 0, 3, 1))