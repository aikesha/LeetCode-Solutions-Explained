# LeetCode 2373: Largest Local Values in a Matrix Solution Explanation

You are given an `n x n` integer matrix `grid`.

Generate an integer matrix `maxLocal` of size `(n - 2) x (n - 2)` such that:

* `maxLocal[i][j]` is equal to the **largest** value of the `3 x 3` matrix in `grid` centered around row `i + 1` and column `j + 1`.

In other words, we want to find the largest value in every contiguous `3 x 3` matrix in `grid`.

Return the *generated matrix*.

**Example 1:**

![example1](https://assets.leetcode.com/uploads/2022/06/21/ex1.png)

> **Input:** grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]

> **Output:** [[9,9],[8,6]]

> **Explanation:** The diagram above shows the original matrix and the generated matrix.
Notice that each value in the generated matrix corresponds to the largest value of a contiguous 3 x 3 matrix in grid.

**Example 2:**

![example2](https://assets.leetcode.com/uploads/2022/07/02/ex2new2.png)

> **Input:** grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]

> **Output:** [[2,2,2],[2,2,2],[2,2,2]]

> **Explanation:** Notice that the 2 is contained within every contiguous 3 x 3 matrix in grid.


## Class and Method Definition
The class `Solution` has a method `largestLocal` which takes a square matrix `grid` as input. This method returns a new matrix consisting of the largest values found in each 3x3 submatrix of the original matrix.


```Python
def largestLocal(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid[0])
    maxLocal = []
    for row in range(n-2):
        temp_arr = []
        for col in range(n-2):
            matrix_3_by_3 = [mat[col:col+3] for mat in grid[row:row+3]]
            max_value = max(max(sub_row) for sub_row in matrix_3_by_3)
            temp_arr.append(max_value)
        maxLocal.append(temp_arr)
    return maxLocal
```

## Solution Breakdown

### 1. Initialize Variables
- `n`: The number of rows and columns in the matrix `grid`.
- `maxLocal`: An initially empty list that will eventually contain the rows of the resulting matrix, with each element representing the largest value in a 3x3 submatrix.

### 2. Iterate Over Possible 3x3 Submatrices
- **Outer Loop**: Iterate over each row where a full 3x3 submatrix can start (`range(n-2)`).
- **Inner Loop**: Iterate over each column where a full 3x3 submatrix can start (`range(n-2)`).

### 3. Extract and Process Each 3x3 Submatrix
- `matrix_3_by_3 = [mat[col:col+3] for mat in grid[row:row+3]]`: This expression extracts each 3x3 submatrix. It slices rows from `row` to `row+3` and columns from `col` to `col+3`.
- `max_value = max(max(sub_row) for sub_row in matrix_3_by_3)`: Calculates the maximum value within the 3x3 submatrix by finding the maximum in each row and then taking the maximum of these values.

### 4. Store the Result
- `temp_arr.append(max_value)`: Append the maximum value of the 3x3 submatrix to `temp_arr`, which stores the results for the current row of the output matrix.
- After processing all columns for the current row, `maxLocal.append(temp_arr)` adds `temp_arr` to `maxLocal`, finalizing the row of the output matrix.

### 5. Return the Result
- The method returns `maxLocal`, which is a matrix of the largest values from each 3x3 submatrix of `grid`.

## Complexity Analysis
- **Time Complexity**: O((n-2)²), as the solution iterates over each element in the `(n-2)x(n-2)` output matrix and processes 9 elements for each.
- **Space Complexity**: O((n-2)²) for storing the output matrix. Additional space usage is minimal as `matrix_3_by_3` and `temp_arr` are reused in each iteration.