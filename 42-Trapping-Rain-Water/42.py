# LeetCode Problem - 42
# Trapping Rain Water

def trapping_rain_water(heights):
    n = len(heights)
    if n<=2:
        return 0
    else:
        left_max_arr = [0]*n
        right_max_arr = [0]*n 
        vol_of_water = 0
        left_max_arr[0] = heights[0]
        right_max_arr[-1] = heights[-1]

        for i in range(1, n):
            left_max_arr[i] = max(left_max_arr[i-1], heights[i])

        i = n-2
        while i>=0:
            right_max_arr[i] = max(right_max_arr[i+1], heights[i])
            i -= 1

        for i in range(1, n-1):
            vol_of_water += min(left_max_arr[i], right_max_arr[i]) - heights[i]

        return vol_of_water


# sample driver code
heights = [int(x) for x in input("Enter the array of heights: ").rstrip().split()]
print(f"Volume of water that can be trapped = {trapping_rain_water(heights)}")