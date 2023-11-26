"""

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0
        for i in range(len(s)):
            # handling odd palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > res_len:
                    res = s[l:r+1]
                    res_len = r-l+1

                l -= 1
                r += 1

            # handling even palindromes
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > res_len:
                    res = s[l:r + 1]
                    res_len = r - l + 1

                l -= 1
                r += 1

        print(res)
        print(res_len)
        return res


if __name__ == "__main__":
    s = Solution()
    out = s.longestPalindrome("bb")
    print(out)