from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = ((1,0), (0,1), (-1, 0), (0, -1))
        count = 0
        q = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    count += 1
                if grid[row][col] == 2:
                    # add neighbours to rot list
                    for direction in directions:
                        next_rot = (row + direction[0], col + direction[1])
                        if next_rot[0] >= 0 and next_rot[0] < len(grid) \
                            and next_rot[1] >= 0 and next_rot[1] < len(grid[0]):
                            q.append(next_rot)
        minutes = 0
        while q:
            next_q = deque()
            did_rot = False
            while q:
                to_rot = q.popleft()
                if grid[to_rot[0]][to_rot[1]] != 1:
                    continue
                did_rot = True
                count -= 1
                grid[to_rot[0]][to_rot[1]] = 2
                for direction in directions:
                    next_rot = (to_rot[0] + direction[0], to_rot[1] + direction[1])
                    if next_rot[0] >= 0 and next_rot[0] < len(grid) \
                        and next_rot[1] >= 0 and next_rot[1] < len(grid[0]):
                        next_q.append(next_rot)
            if did_rot:
                minutes += 1
            q = next_q
        
        if count > 0:
            return -1
        return minutes
        
grid = [[2,2],[1,1],[0,0],[2,0]]
print(Solution().orangesRotting(grid))