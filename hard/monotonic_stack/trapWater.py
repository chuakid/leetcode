def trap(height) -> int:
    mono_stack = []
    total = 0
    for i, v in enumerate(height):
        while mono_stack and height[mono_stack[-1]] < v:
            prev = mono_stack.pop()
            if not mono_stack:
                break
            h = min(height[mono_stack[-1]] - height[prev], v - height[prev])
            w = i - mono_stack[-1] - 1
            total += h * w
        mono_stack.append(i)
    return total


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
