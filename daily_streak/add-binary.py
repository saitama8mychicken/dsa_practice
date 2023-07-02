"""
Given two binary strings a and b, return their sum as a binary string.


"""

class Solution:
    def get_binary(self, numeric_sum):
        if numeric_sum == 2:
            return 10
        elif numeric_sum == 3:
            return 11
        elif numeric_sum == 1:
            return 1
        else:
            return 0

    def addBinary(self, a: str, b: str) -> str:
        print("new", a, b)
        max_digits = a if len(a) > len(b) else b
        res = ""
        carry = 0
        for i in range(len(max_digits)):
            digit_sum = carry

            if i < len(a):
                digit_sum += int(a[len(a) - i - 1])

            if i < len(b):
                digit_sum += int(b[len(b) - i - 1])

            binary_sum = self.get_binary(digit_sum)
            # print("printing sum", a, b, digit_sum, binary_sum, res, carry, "===")
            res = str(binary_sum % 10) + res
            carry = binary_sum // 10

        if carry:
            res = str(carry) + res

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.addBinary("11", "1"), "100")
    print(s.addBinary("1010", "1011"), "10101")