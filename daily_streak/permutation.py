"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]

"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        # base condition
        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)

            result.extend(perms)
            nums.append(n)

        return result

# explain above code
# nums = [1,2,3]




if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3]
    print(s.permute(nums))
    #
    # nums = [0,1]
    # print(s.permute(nums))
    #
    # nums = [1]
    # print(s.permute(nums))
    #
    # nums = [1,2,3,4]
    # print(s.permute(nums))
    #
    #