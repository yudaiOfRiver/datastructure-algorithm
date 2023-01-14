def binary_search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l+r) // 2
        if target == nums[m]:
            return m
        elif target < nums[m]:
            r = m-1
        elif nums[m] < target:
            l = m+1
    return l
