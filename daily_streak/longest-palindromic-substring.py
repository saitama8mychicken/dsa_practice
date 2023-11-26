"""

"""


class Solution:
    @staticmethod
    def check_if_palindrome(str_):
        return str_ == str_[::-1]

    def longestPalindrome(self, s: str) -> str:
        res = ""

        if len(s) == 1:
            return s

        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                str_ = s[i:j]
                print(str_, self.check_if_palindrome(str_), max(str_, res))
                if self.check_if_palindrome(str_):
                    if len(str_) > len(res):
                        res = str_

        return res


if __name__ == "__main__":
    s = Solution()
    out = s.longestPalindrome("bb")
    print(out)