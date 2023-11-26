"""

"""
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        concatenated_strings = []
        res = set()

        def backtrack(word_list, path):
            if len(word_list) == 0:
                concatenated_strings.append("".join(path))
                return
            for ind, word in enumerate(word_list):
                backtrack(word_list[:ind] + word_list[ind + 1:], path + [word])

        backtrack(words, [])
        common_length = len(concatenated_strings[0])

        for char_ind, char in enumerate(s):
            for ind, concatenated_string in enumerate(concatenated_strings):
                if s[char_ind:char_ind+common_length] == concatenated_string:
                    res.add(char_ind)

        return list(res)



if __name__ == "__main__":
    s = Solution()
    out = s.findSubstring("barfoothefoobarman", ["foo", "bar"])
    print(out)

