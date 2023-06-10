"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.



Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

question: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
solution: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/967973951/
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # using two pointer
        left = 0
        right = len(numbers)-1

        while left <= right:
            if numbers[left]+numbers[right] > target:
                right -= 1

            elif numbers[left]+numbers[right] < target:
                left += 1

            else:
                return [left+1, right+1]


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))
    print(s.twoSum([2,3,4], 6))
    print(s.twoSum([-1,0], -1))
    print(s.twoSum([5,25,75], 100))
    print(s.twoSum([1,2,3,4,4,9,56,90], 8))
    print(s.twoSum([1,2,3,4,4,9,56,90], 10))
    print(s.twoSum([1,2,3,4,4,9,56,90], 11))
    print(s.twoSum([1,2,3,4,4,9,56,90], 12))
    print(s.twoSum([1,2,3,4,4,9,56,90], 13))
    print(s.twoSum([1,2,3,4,4,9,56,90], 14))
    print(s.twoSum([1,2,3,4,4,9,56,90], 15))
    print(s.twoSum([1,2,3,4,4,9,56,90], 16))
    print(s.twoSum([1,2,3,4,4,9,56,90], 17))
    print(s.twoSum([1,2,3,4,4,9,56,90], 18))
    print(s.twoSum([1,2,3,4,4,9,56,90], 19))
    print(s.twoSum([1,2,3,4,4,9,56,90], 20))
    print(s.twoSum([1,2,3,4,4,9,56,90], 21))
    print(s.twoSum([1,2,3,4,4,9,56,90], 22))
    print(s.twoSum([1,2,3,4,4,9,56,90], 23))
    print(s.twoSum([1,2,3,4,4,9,56,90], 24))
    print(s.twoSum([1,2,3,4,4,9,56,90], 25))