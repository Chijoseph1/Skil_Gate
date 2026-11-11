def insert(nums):
    comparisons = 0
    shift = 0

    for i in range(1,len(nums)):
        j = i
        while j > 0:
            comparisons += 1
            if nums[j-1] > nums[j]:
                nums[j-1],nums[j] = nums[j],nums[j-1]
                shift += 1
                j -= 1
            else:
                break
    return (comparisons,shift)

print(insert([5,2,4,1]))