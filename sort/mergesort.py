def mergesort(nums):

    def merge(left, right):
        lp, rp = 0, 0
        merged = []
        while lp < len(left) and rp < len(right):
            if left[lp] <= right[rp]:
                merged.append(left[lp])
                lp += 1
            else:
                merged.append(right[rp])
                rp += 1

        if lp < len(left):
            merged.extend(left[lp:])
        elif rp < len(right):
            merged.extend(right[rp])
        return merged


    if len(nums) == 1:
        return nums

    m = len(nums) // 2
    left, right = nums[:m], nums[m:]
    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)



nums = [2, 6, 3, 7, -1, 4, 0]
print(mergesort(nums))





