class Solution:
    def maximumBags(self, capacity, rocks, additionalRocks: int) -> int:
        for i in range(len(capacity)):
            capacity[i] = capacity[i] - rocks[i]
        capacity.sort()
        total_bags = 0
        for rocks_needed in capacity:
            if rocks_needed == 0:
                total_bags += 1
            elif rocks_needed <= additionalRocks:
                additionalRocks -= rocks_needed
                total_bags += 1
            else:
                return total_bags
        return total_bags
