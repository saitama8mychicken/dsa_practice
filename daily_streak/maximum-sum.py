"""

"""

class Solution:

    def __init__(self):
        self.max_sum = 0

    def maximumSubsequenceSum(self, nums):
        self.max_sum = nums[0]
        self.backtrack(nums, [])
        return self.max_sum

    def backtrack(self,numbers, path):
        print(numbers, path)
        if sum(path) > self.max_sum:
            self.max_sum = sum(path)

        for i in range(len(numbers)):
            self.backtrack(numbers[i+2:], path + [numbers[i]])


if __name__ == "__main__":
    s = Solution()
    nums = [3, 2, 7, 10]
    print(s.maximumSubsequenceSum(nums))