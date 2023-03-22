import numpy as np

def quick_sort(nums):
    if len(nums) <= 1:
        return nums

    pivot = np.random.choice(nums)
    pivot_count = 0

    left = []; right = []
    for num in nums:
        if num < pivot: left.append(num)
        if num > pivot: right.append(num)
        if num == pivot: pivot_count += 1

    return quick_sort(left) + [pivot] * pivot_count + quick_sort(right)


nums = [2, 2, 1, 6, 1, 7, 3]
print(quick_sort(nums))


