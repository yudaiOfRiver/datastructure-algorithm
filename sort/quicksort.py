import random

def quicksort(nums):
    if len(nums) == 0:
        return nums

    base = random.choice(nums)
    base_count = 0
    left, right = [], []

    for num in nums:
        if num < base:
            left.append(num)
        elif num > base:
            right.append(num)
        else:
            base_count += 1

    left = quicksort(left)
    right = quicksort(right)
    return left + [base] * base_count + right

nums = [2, 2, 1, 6, 1, 7, 3]
print(quicksort(nums))


