# LeetCode Problem - 59
# Spiral Matrix - II

def spiral_matrix(n):

    matrix = []
    for i in range(n):
        arr = []
        for j in range(n):
            arr.append(0)
        matrix.append(arr)
         
    totalLayers = (n+1)//2
    fillValue = 1
    for currentLayer in range(totalLayers):

        # left -> right
        for i in range(currentLayer, n-currentLayer):
            matrix[currentLayer][i] = fillValue
            fillValue += 1

        # top to bottom
        for i in range(currentLayer+1, n-currentLayer):
            matrix[i][n-1-currentLayer] = fillValue
            fillValue += 1

        # right to left
        i = n-currentLayer-2
        while i>=currentLayer:
            matrix[n-1-currentLayer][i] = fillValue
            fillValue += 1
            i -= 1

        # bottom to top
        i = n-currentLayer-2
        while i>currentLayer:
            matrix[i][currentLayer] = fillValue
            fillValue += 1
            i -= 1

    return matrix


# driver code
n = int(input("Enter the value of n: "))
print(f"The matrix is: {spiral_matrix(n)}")