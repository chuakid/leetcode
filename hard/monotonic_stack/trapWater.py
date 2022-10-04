# water can only be trapped between two walls that are taller than the middle walls
# thus, when a wall is higher than the previous walls, water will be trapped between the previous wall that's taller than the current wall and the current wall
# therefore, decreasing monotonic stack is suitable as we need only need to check for trapped water next wall is taller, and water cannot be trapped there twice

def trap(height) -> int:
    mono_stack = []
    total = 0
    for i, v in enumerate(height):
        # if next wall is taller than previous wall, pop until previous wall is taller
        while mono_stack and height[mono_stack[-1]] < v:
            prev = mono_stack.pop()
            # if no previous wall to be left wall
            if not mono_stack:
                break
            # water will be trapped from the height of the middle wall to the height of the lower wall
            # if the lower wall == middle wall, no water is trapped between them  _ _ |, h will be 0
            h = min(height[mono_stack[-1]] - height[prev], v - height[prev])
            w = i - mono_stack[-1] - 1
            total += h * w
        mono_stack.append(i)
    return total


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
