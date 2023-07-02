"""

"""
from typing import List

class Solution:
     def letterCombinations(self, digits: str) -> List[str]:
         if (len(digits) == 0):
             return []
         hashmap = {
             "2": "abc",
             "3": "def",
             "4": "ghi",
             "5": "jkl",
             "6": "mno",
             "7": "pqrs",
             "8": "tuv",
             "9": "wxyz",
         }
         ans = []
         current_str = ""

         def recursive(digits, ans, hashmap, current_str, i):
             if len(current_str) == len(digits):
                 ans.append(current_str)
                 return

             string = hashmap[digits[i]]

             for j in range(len(string)):
                 recursive(digits, ans, hashmap, current_str + string[j], i + 1)

         recursive(digits, ans, hashmap, current_str, 0)
         return ans


if __name__ == "__main__":

    s = Solution()
    digits = "23"
    print(s.letterCombinations(digits))
