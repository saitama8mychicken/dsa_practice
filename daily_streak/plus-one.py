"""
66. Plus One
Easy
7.5K
5K
Companies
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

"""
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        output_dict = []
        carry = 1
        for i in range(len(digits)):
            index_from_last = len(digits) - i -1
            number = digits[index_from_last]

            number = number + carry

            carry = number // 10
            number_to_add = number % 10

            output_dict.append(number_to_add)

        if carry :
            output_dict.append(carry)

        return output_dict[::-1]


if __name__ == "__main__":
    s = Solution()
    s.plusOne([9])

