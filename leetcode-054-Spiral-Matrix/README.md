# Spiral Matrix Solution Explanation

Given an `m x n` `matrix`, return *all elements of the* `matrix` *in spiral order.*

**Example 1:**

![example1](https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg)

> **Input:** matrix = [[1,2,3],[4,5,6],[7,8,9]]

> **Output:** [1,2,3,6,9,8,7,4,5]

**Example 2:**

![example2](https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg)

> **Input:** matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

> **Output:** [1,2,3,4,8,12,11,10,9,5,6,7]


## Version 1: Direct Manipulation

```Python
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
```

### Reasoning
This approach directly manipulates the matrix by sequentially removing rows or columns that represent the next part of the spiral order. The idea is to reduce the dimension of the matrix in each step while collecting the elements in the spiral sequence.

### Approach
1. **Remove the First Row**: The top row of the matrix is removed and its elements are added to the result.
2. **Remove the Last Column**: The last column is iterated through, and elements are added to the result. This column is then removed from the matrix.
3. **Remove the Last Row**: If still available, the bottom row is removed, reversed, and its elements are added to the result.
4. **Remove the First Column**: Finally, the first column is iterated through in reverse order, and those elements are added to the result. This column is then removed from the matrix.
5. The process repeats until all rows and columns are processed.

### Example
For the matrix:

![example1](https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg)

> **Input:** matrix = [[1,2,3],[4,5,6],[7,8,9]]

> **Output:** [1,2,3,6,9,8,7,4,5]
- Extract `1, 2, 3`, then `6, 9`, reverse `8, 7`, and reverse `4, 5` to get `[1, 2, 3, 6, 9, 8, 7, 4, 5]`.

### Complexity
- **Time Complexity**: O(m*n), where m is the number of rows and n is the number of columns, because each element is processed exactly once.
- **Space Complexity**: O(1) excluding the output array. The input matrix is modified in place.


## Version 2: Simplified Direct Manipulation

```Python
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
```

### Reasoning
This version simplifies the manipulation by consistently removing elements from the matrix without individually tracking matrix dimensions.

### Approach
1. **Remove the First Row**: Directly pop and append the first row to the result.
2. **Remove the Last Column**: Traverse down what remains of the matrix, popping the last element of each row.
3. **Remove the Last Row**: If any rows are left, pop and reverse the last row, then append it.
4. **Remove the First Column**: If there are remaining rows, traverse up the matrix, popping the first element of each.
5. Repeat until the matrix is empty.

### Example
Using the same matrix as before, the method is similar but implemented with simpler operations that handle matrix boundaries implicitly.

### Complexity
- **Time Complexity**: O(m*n), with each element being visited once.
- **Space Complexity**: O(1) excluding the output array, as the matrix is modified in place but not copied.