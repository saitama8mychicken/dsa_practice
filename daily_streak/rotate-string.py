"""
Rotate String
"""

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        for i in range(len(s)):
            shifted_string = s[i:] + s[:i]
            # print(shifted_string)

            if shifted_string == goal:
                return True

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.rotateString("abcde", "cdeab"), True)
    print(s.rotateString("abcde", "abced"), False)