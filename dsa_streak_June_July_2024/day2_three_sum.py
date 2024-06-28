class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        three_sum = set()

        nums_dict = {}
        for ind, num in enumerate(nums):
            if num in nums_dict:
                nums_dict[num].append(ind)
            else:
                nums_dict[num] = [ind]


        for i, num1 in enumerate(nums):
            # lets find 2 sum for same
            required_sum = -1 * num1
            for j, num2 in enumerate( nums[i:], i):
                num3 = required_sum-num2
                if num3 in nums_dict:
                    for k in nums_dict[num3]:
                        if i != j != k != i:
                            res = [num1, num2, required_sum-num2]
                            res.sort()
                            res = tuple(res)
                            if res not in three_sum:
                                three_sum.add(res)                      
        return three_sum

