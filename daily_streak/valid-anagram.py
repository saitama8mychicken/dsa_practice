"""
242. Valid Anagram
Easy
9.3K
292
Companies
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        temp_dict = {}

        for char_ in s:
            if char_ in temp_dict:
                temp_dict[char_] += 1
            else:
                temp_dict[char_] = 1

        for char_ in t:
            if char_ in temp_dict:
                temp_dict[char_] -= 1
            else:
                return False

        for key, val in temp_dict.items():
            if val != 0:
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))
