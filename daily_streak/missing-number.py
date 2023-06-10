"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.



Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

https://leetcode.com/problems/missing-number/submissions/967554733/
"""

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # will find the sum of possible list and then substract all numbers from that

        sum = int(len(nums) * (len(nums) + 1)/2)

        for num in nums:
            sum -= num

        return sum
