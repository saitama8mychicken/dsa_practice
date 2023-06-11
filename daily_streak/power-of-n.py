"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).



Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


link : https://leetcode.com/problems/powx-n/
Category: Medium
Type: Recursion
"""
class Solution:
    def calculate_power(self, x, n):
        if n == 0: return 1
        if x == 0: return 0

        res = self.calculate_power(x*x, n // 2)

        return x*res if n%2 else res

    def myPow(self, x: float, n: int) -> float:

        if n > 0:
            return self.calculate_power(x, n)
        else:
            return 1/self.calculate_power(x,n*-1)


if __name__ == "__main__":
    s = Solution()
    print(s.myPow(2.00000, 10))