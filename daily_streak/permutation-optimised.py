"""

"""
from typing import List

class Solution:
    def __init__(self):
        self.result = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, [])
        return self.result

    def backtrack(self, nums, path):
        if len(nums) == 0:
            self.result.append(path)

        for i in range(len(nums)):
            self.backtrack(nums[:i] + nums[i+1:], path+[nums[i]])



if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3]
    print(s.permute(nums))

    # nums = [0,1]
    # print(s.permute(nums))
    #
    # nums = [1]
    # print(s.permute(nums))
    #
    # nums = [1,2,3,4]
    # print(s.permute(nums))
    #

