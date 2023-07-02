"""

"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        string_ind = 0
        last_char = ""
        for patter_ind, char in enumerate(p):
            if char == '?':
                string_ind += 1
            elif char == "*":
                pass
            elif last_char == "*" and char != "*":
                while s[string_ind] != char:
                    string_ind += 1
                    if string_ind >= len(s):
                        return False
            else:
                if s[string_ind] == char:
                    string_ind += 1
                else:
                    return False
            last_char = char

        if last_char == "*":
            return True
        elif string_ind == len(s):
            return True
        else:
            return False
