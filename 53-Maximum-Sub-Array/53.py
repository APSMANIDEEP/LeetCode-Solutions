def maximum_sub_array(nums):
    n = len(nums)
    if n==1:
        return nums[0]
    
    for i in range(n):
        nums[i] += max(0, nums[i-1])
    
    return max(nums)

# driver code
nums = [int(x) for x in input("Enter the array: ").rstrip().split()]
print(f"The maximum sub array sum is: {maximum_sub_array(nums)}")
