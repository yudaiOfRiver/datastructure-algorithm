def bubblesort(nums):

    change = True
    while change:
        change = False
        for i in range(len(nums)-1):
            print(nums)
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                change = True

    return nums

nums = [2, 6, 3, 7, -1, 4, 0]
bubblesort(nums)


