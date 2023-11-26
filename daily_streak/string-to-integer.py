"""

"""


class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        current_ind = 0
        is_positive = 1
        found_int = False
        while current_ind < len(s):
            char = s[current_ind]

            if char == "-" and not found_int:
                is_positive = -1
                found_int = True
            elif char == "+" and not found_int:
                is_positive = +1
                found_int = True

            elif (ord(char) - ord('0')) <= 9 and (ord(char) - ord('0')) >= 0:
                int_value = ord(char) - ord('0')
                res *= 10
                res += int_value
                found_int = True
            elif char == " " and not found_int:  # since + was skipped
                ...
            else:
                break

            current_ind += 1

        res = res * is_positive

        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        if res > INT_MAX:  # if ans > 2^31 - 1
            res = INT_MAX

        if res < INT_MIN:  # if ans < -2^31
            res = INT_MIN

        return res

