def binary_search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l+r) // 2
        if target == nums[m]:
            return m
        elif nums[m] > target:
            r = m-1
        elif nums[m] < target:
            l = m+1
#    return None # 値がなければ None を返す
    return l     # 値がなければ 挿入箇所 を返す


if __name__ == '__main__':
    nums = [1, 3, 4, 6, 7, 8]
    print(binary_search(nums, 1))
    print(binary_search(nums, 6))
    print(binary_search(nums, 8))
    print(binary_search(nums, 5))
