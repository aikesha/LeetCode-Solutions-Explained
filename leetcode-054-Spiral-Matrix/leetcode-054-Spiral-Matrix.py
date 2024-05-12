from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    # Original shape: (m, n)
    m = len(matrix)    # row length
    n = len(matrix[0]) # column length
    spiralMatrix = []
    while m > 0:
        # Extending spital Matrix and Removing first row --> shape becomes (m-1, n)
        curr_row = matrix[0]
        spiralMatrix.extend(curr_row)
        matrix.remove(curr_row)
        m -= 1

        if n > 0:
            # Extending spital Matrix and Removing last column --> shape becomes (m-1, n-1)
            curr_col = [row[n-1] for row in matrix]
            spiralMatrix.extend(curr_col)
            [r.pop(n-1) for r in matrix]
            n -= 1

        if m > 0:
            # Extending spital Matrix and Removing last row --> shape becomes (m-2, n-1)
            curr_row = matrix[m-1]
            spiralMatrix.extend(curr_row[::-1])
            matrix.remove(curr_row)
            m -= 1

        if n > 0:
            # Extending spital Matrix and Removing first column --> shape becomes (m-2, n-2)
            curr_col = [row[0] for row in matrix]
            spiralMatrix.extend(curr_col[::-1])
            [r.pop(0) for r in matrix]
            n -= 1
    return spiralMatrix
    
    
def spiralOrder2(matrix: List[List[int]]) -> List[int]:
    result = []
    while matrix:
        # Remove the first row and extend result with it
        result += matrix.pop(0)
        
        # If there's anything left in the matrix, process the rightmost column
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        
        # If there's anything left, remove the last row and extend result with it reversed
        if matrix:
            result += matrix.pop()[::-1]
        
        # If there's anything left, process the leftmost column in reverse order
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    
    return result


print('=================Version 1 Outputs==================')
# Test cases
case1 = [[1,2,3],[4,5,6],[7,8,9]] # Expected Output1: [1,2,3,6,9,8,7,4,5]
case2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] # Expected Output2: [1,2,3,4,8,12,11,10,9,5,6,7]
case3 = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]] # Expected Output3: [1,2,3,4,5,6,7,8,9,10]

for case in [case1, case2, case3]:
    print(spiralOrder(case))
    
    
print('=============Version 2 (simple) Outputs=============')
# Test cases
case1 = [[1,2,3],[4,5,6],[7,8,9]]  # Expected Output: [1,2,3,6,9,8,7,4,5]
case2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]  # Expected Output: [1,2,3,4,8,12,11,10,9,5,6,7]
case3 = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]  # Expected Output: [1,2,3,4,5,6,7,8,9,10]

print("Output for Case 1:", spiralOrder2([row[:] for row in case1]))
print("Output for Case 2:", spiralOrder2([row[:] for row in case2]))
print("Output for Case 3:", spiralOrder2([row[:] for row in case3]))