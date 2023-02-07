

def totalFruit(fruits: list[int]) -> int:
    """
    Sliding window technique

    Left of window changes only when right is a new fruit that isn't the current two fruits.
    Left shifts to the "next_left_pos", which changes whenever
    a new fruit is seen that isn't the last next_left_fruit.
    """

    total_max, left, right = 0, 0, 0
    fruit1, fruit2 = fruits[0], fruits[0]
    next_left_fruit, next_left_pos = fruit2, 0
    curr_max = 0
    while right < len(fruits):
        new_fruit = fruits[right]
        if fruit1 == fruit2 and new_fruit != fruit1:
            fruit2 = fruits[right]
            next_left_fruit = fruit2
            next_left_pos = right
        elif new_fruit != fruit1 and new_fruit != fruit2:
            # move left to next_left
            left = next_left_pos
            fruit1, fruit2 = next_left_fruit, new_fruit
            next_left_fruit, next_left_pos = new_fruit, right
            curr_max = right - left
        else:
            if new_fruit != next_left_fruit:
                next_left_fruit = new_fruit
                next_left_pos = right

        curr_max += 1
        total_max = max(curr_max, total_max)
        right += 1

    return total_max


ans = totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4])
assert(ans == 5)
ans = totalFruit([0, 1, 2, 2])
assert(ans == 3)
ans = totalFruit([1, 0, 1, 4, 1, 4, 1, 2, 3])
assert(ans == 5)
