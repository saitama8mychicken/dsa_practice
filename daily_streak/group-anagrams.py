"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]

"""
from typing import  List


class Solution:
    def check_if_anagram(self, str1, str2):
        char_dict = {}
        for char in str1:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

        for char in str2:
            if char in char_dict:
                char_dict[char] -= 1
            else:
                return False

        for char, count in char_dict.items():
            if count != 0:
                return False

        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_groups = []
        for str_ in strs:
            found_anagram_group = False
            for anagram_group in anagram_groups:
                if self.check_if_anagram(anagram_group[0], str_):
                    anagram_group.append(str_)
                    found_anagram_group = True

            if not found_anagram_group:
                anagram_groups.append([str_])

        return anagram_groups


if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["","b",""]))