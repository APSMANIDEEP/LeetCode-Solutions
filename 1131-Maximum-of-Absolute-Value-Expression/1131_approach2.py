# main code function
def max_abs_value_exp(arr1, arr2, n):
    
    # set a maximum value limit and start comparing with that
    max1 = max2 = max3 = max4 = -2**31

    # set a minimum value limit and start comparing with that
    min1 = min2 = min3 = min4 = (2**31-1)

    for i in range(n):
        exp1 = arr1[i] + arr2[i] + i 
        max1 = max(exp1, max1)
        min1 = min(exp1, min1)

        exp2 = arr1[i] + arr2[i] - i 
        max2 = max(exp2, max2)
        min2 = min(exp2, min2)

        exp3 = arr1[i] - arr2[i] + i 
        max3 = max(exp3, max3)
        min3 = min(exp3, min3)

        exp4 = arr1[i] + arr2[i] + i 
        max4 = max(exp4, max4)
        min4 = min(exp4, min4)

    max_ans = max(max1-min1, max2-min2, max3-min3, max4-min4)
    return max_ans


# sample driver code -- created for your freedom to give your own input
# but make sure both the arrays are of same length
n = int(input("Enter the size of arrays: "))
arr1 = [int(x) for x in input(f"Enter the first array of length {n}: ").rstrip().split()]
arr2 = [int(x) for x in input(f"Enter the second array of length {n}: ").rstrip().split()]
print(max_abs_value_exp(arr1, arr2, n))