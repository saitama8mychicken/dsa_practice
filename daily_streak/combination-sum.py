"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.



Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []


Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40

"""
from typing import List


class Solution:

    def __init__(self):
        self.target = 0
        self.result = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.target = target
        self.backtrack(candidates, [])
        return self.result

    def backtrack(self, nums, path):
        if sum(path) == self.target:
            self.result.append(path)
            return
        else:
            for num in nums:
                if sum(path) + num <= self.target:  # make sure the sum of the path is less than or equal to the target
                    if len(path) > 0:
                        if num >= path[-1]:  # make sure the next number is greater than or equal to the last number in the path so as to prevent repetition
                            self.backtrack(nums, path + [num])
                    else:
                        self.backtrack(nums, path + [num])


if __name__ == "__main__":
    s = Solution()
    candidate = [2,3,6,7]
    targets = 7
    print(s.combinationSum(candidate, targets))




