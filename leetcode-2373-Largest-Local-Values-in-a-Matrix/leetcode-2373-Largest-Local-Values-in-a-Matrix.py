from typing import List

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

case1 = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]] # Expected Out1: [[9,9],[8,6]]
case2 = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]] # Expected Out2: [[2,2,2],[2,2,2],[2,2,2]]

for case in [case1, case2]:
    print(largestLocal(case))