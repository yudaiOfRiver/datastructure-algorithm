def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid   = len(nums) // 2
    left  = nums[:mid]
    right = nums[mid:]

    left  = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    i = j = 0
    merged = []
    # 2つの配列を比較しながらマージする
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # 残った要素を追加する
    merged += left[i:]
    merged += right[j:]
    return merged


nums = [100, -29, 0, 7, -1, 4, 0, 23, -29]
print(merge_sort(nums))





