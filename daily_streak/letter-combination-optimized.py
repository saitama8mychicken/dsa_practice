"""

"""
from typing import List

class Solution:

    def __init__(self):
        self.result = []
        self.digits = ""

    def get_corresponding_letters(self, digit):
        if digit == "2":
            return ['a', 'b', 'c']

        if digit == "3":
            return ['d', 'e', 'f']

        if digit == "4":
            return ['g', 'h', 'i']

        if digit == "5":
            return ['j', 'k', 'l']

        if digit == "6":
            return ['m', 'n', 'o']

        if digit == "7":
            return ['p', 'q', 'r', 's']

        if digit == "8":
            return ['t', 'u', 'v']

        if digit == "9":
            return ['w', 'x', 'y', 'z']

    def letterCombinations(self, digits):
        self.digits = digits
        self.backtrack(0, [])
        return self.result

    def backtrack(self, current_ind, path):
        if len(path) == len(self.digits):
            self.result.append(path)
            return
        else:
            letters = self.get_corresponding_letters(self.digits[current_ind])
            for i in range(len(letters)):
                self.backtrack(current_ind+1, path + [letters[i]])



if __name__ == "__main__":

    s = Solution()
    digit = "234"
    print(s.letterCombinations(digit))
