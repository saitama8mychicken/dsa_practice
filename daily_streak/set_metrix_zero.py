"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.



Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        index_with_zero_value = []
        rows = len(matrix)
        cols = len(matrix[0])

        # finding index with value zero
        for row_index, row in enumerate(matrix):
            for col_index, col_val in enumerate(row):
                if col_val == 0:
                    index_with_zero_value.append((row_index, col_index))

        # create indexs where to apply zero
        index_to_apply_zero = []

        for index in index_with_zero_value:
            row = index[0]
            col = index[1]
            for i in range(rows):
                index_to_apply_zero.append((i, col))

            for i in range(cols):
                index_to_apply_zero.append((row, i))

        # apply zero to all the above indexes
        for index in index_to_apply_zero:
            matrix[index[0]][index[1]] = 0


if __name__ == "__main__":
    s = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    s.setZeroes(matrix)
