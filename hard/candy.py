def candy(ratings: list[int]) -> int:
    """
    Do first pass from left to right, where if i-th rating > i-1-th rating, left_to_right[i] = left_to_right[i-1]
    This means that if i-th rating is higher than its left neighbour, it should have 1 more candy than the left neighbour.
    Do second pass right to left, but with right neighbours.

    For each rating, the candy that child should have is equal to max(left_to_right[i], right_to_left[i]) to satisfy both left and right
    constraints.
    """
    left_to_right, right_to_left = [1 for _ in range(len(ratings))], [
        1 for _ in range(len(ratings))]
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            left_to_right[i] = left_to_right[i - 1] + 1
    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            right_to_left[i] = right_to_left[i + 1] + 1
    ans = 0
    for a, b in zip(left_to_right, right_to_left):
        ans += max(a, b)
    return ans


ans = candy([1, 0, 2])
assert ans == 5, ans
