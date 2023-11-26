"""

"""
from typing import List


class Solution:

    def find_common_substring(self, str1, str2):
        common_string = ""

        for i in range(len(str1)):
            if i < len(str1):
                char1 = str1[i]
            else:
                return common_string

            if i < len(str2):
                char2 = str2[i]
            else:
                return common_string

            if char1 == char2:
                common_string += char1
            else:
                return common_string

        return common_string

    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = strs[0]
        for str_ in strs[1:]:
            common_prefix = self.find_common_substring(common_prefix, str_)

            if common_prefix == "":
                return common_prefix

        return common_prefix


if __name__ == "__main__":
    s = Solution()
    # print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    # print(s.longestCommonPrefix(["dog", "racecar", "car"]))
    # print(s.longestCommonPrefix([""]))
    print(s.longestCommonPrefix(["",""]))