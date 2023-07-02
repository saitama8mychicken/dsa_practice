"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Given a roman numeral, convert it to an integer.

"""


class Solution:
    def get_int_for_roman(self, roman):

        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        return roman_dict.get(roman, 0)

    def romanToInt(self, s: str) -> int:
        res = 0
        for i in range(len(s) - 1):

            if self.get_int_for_roman(s[i]) < self.get_int_for_roman(s[i + 1]):
                res -= self.get_int_for_roman(s[i])

            else:
                res += self.get_int_for_roman(s[i])

        return res + self.get_int_for_roman(s[-1])


if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("MCMXCIV"), 1994)
    print(s.romanToInt("LVIII"), 58)
    print(s.romanToInt("IX"), 9)
    print(s.romanToInt("IV"), 4)
    print(s.romanToInt("III"), 3)
    print(s.romanToInt("I"), 1)
    print(s.romanToInt("V"), 5)
    print(s.romanToInt("X"), 10)
    print(s.romanToInt("L"), 50)
    print(s.romanToInt("C"), 100)
    print(s.romanToInt("D"), 500)