def min_missing_positive(nums):
    nums.sort()  
    missing = 1 
    for num in nums:
        if num == missing:
            missing += 1 
        elif num > missing:
            return missing
    return missing