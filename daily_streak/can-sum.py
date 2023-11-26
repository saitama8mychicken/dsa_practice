"""
This is a can sum problem

"""

from typing import List

class Solution:

    def canSum(self, target, numbers, memo = {}):
        if memo.get(target) != None:
            return memo[target]

        if target == 0:
            return True
        if target < 0:
            return False

        for number in numbers:
            reminder = target - number
            res = self.canSum(reminder, numbers)
            memo[target] = res
            if res is True:
                return True

        memo[target] = False
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.canSum(7, [2, 3]))
    print(s.canSum(20, [2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(s.canSum(300, [7, 14]))
    print(s.canSum(300, [7, 12]))
