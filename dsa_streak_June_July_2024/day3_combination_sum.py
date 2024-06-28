class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []

        def backtrack(nums, history, target):
            for i, num in enumerate(nums):
                if target - num > 0:
                    backtrack(nums[i:], history+[num], target-num)
                elif target-num == 0:
                    output.append(history+[num])

        backtrack(candidates, [], target)
        return output
