"""
This is a grid traveller question.

You are given a m*n grid. You can only move down or right. How many ways are there to reach the bottom right corner from top left corner?

"""

from typing import List


class Solution:
    def __init__(self):
        self.paths = 0

    def grid_traveller(self, m: int, n: int) -> int:

        total_routes = []

        def backtrack(rows, cols, memo = {}):
            if (rows, cols) in memo:
                return memo[rows, cols]
            if rows==1 and cols ==1:
                return 1
            elif rows == 0 or cols == 0:
                return 0
            else:
                # move right
                right_step = backtrack(rows-1, cols)

                # move down
                down_step = backtrack(rows, cols-1)

                res = right_step+down_step

                memo[(rows,cols)] = res

                return res

        return backtrack(m, n)


if __name__ == "__main__":
    s = Solution()
    m = 20
    n = 300
    print(s.grid_traveller(m, n))
    # print(s.permute(nums))
    #
    # nums = [1]
    # print(s.permute(nums))










