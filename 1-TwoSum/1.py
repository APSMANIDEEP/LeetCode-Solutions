arr = [int(x) for x in input("Enter the array: ").rstrip().split()]
target = int(input("Enter the target sum: "))
hashmap = {}

for i in range(len(arr)):
    x = target - arr[i]
    if x in hashmap.values():
        print([i, arr.index(x)])
        break
    else:
        hashmap[i] = arr[i]
