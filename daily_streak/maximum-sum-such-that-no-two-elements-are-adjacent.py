"""
Given an array arr[] of positive numbers, The task is to find the maximum sum of a subsequence such that no 2 numbers in the sequence should be adjacent in the array.

Examples:

Input: arr[] = {5, 5, 10, 100, 10, 5}
Output: 110
Explanation: Pick the subsequence {5, 100, 5}.
The sum is 110 and no two elements are adjacent. This is the highest possible sum.

Input: arr[] = {3, 2, 7, 10}
Output: 13
Explanation: The subsequence is {3, 10}. This gives sum = 13.
This is the highest possible sum of a subsequence following the given criteria


"""

from typing import List

class Solution:

    def __init__(self):
        self.maximum_sum = 0
    def maximum_sum(self, arr: List[int]) -> int:
        self.maximum_sum = arr[0]

        def backtrack(arr, current_ind, path):
            if current_ind >= len(arr)-2:
                maximum_sum = max(self.maximum_sum, sum(path))
            else:
                for i in range(len(arr)):
                    backtrack(arr, i, path+[arr[i]])

        backtrack(arr, 0, [])

        return self.maximum_sum

