def largestRectangleArea(heights) -> int:
    ret = 0
    heights.append(0)
    mono_stack = []
    for i, v in enumerate(heights):
        while mono_stack and v < heights[mono_stack[-1]]:
            height = heights[mono_stack.pop()]
            width = i - mono_stack[-1] - 1 if mono_stack else i
            ret = max(width*height, ret)
        mono_stack.append(i)

    return ret


# largestRectangleArea([2, 1, 5, 6, 2, 3])
