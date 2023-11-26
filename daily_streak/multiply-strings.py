"""

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.


"""


class Solution:

    def convert_to_integer(self, char):
        return ord(char) - ord('0')

    def multiply(self, num1: str, num2: str) -> str:
        max_len = len(num1) if len(num1) > len(num2) else len(num2)
        carry = 0
        res = 0
        num1_int = 0
        num2_int = 0
        for i in range(max_len):
            char_1 = self.convert_to_integer(num1[len(num1) - i - 1] if i < len(num1) else '1')
            char_2 = self.convert_to_integer(num2[len(num2) - i - 1] if i < len(num2) else '1')

            num2_int = num2_int * 10 + char_2
            num1_int = num1_int * 10 + char_1

        return str(num1_int * num2_int)


if __name__ == "__main__":
    s = Solution()
    print(s.multiply("123", "456"))
