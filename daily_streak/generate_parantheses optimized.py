"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8

question-link: https://leetcode.com/problems/generate-parentheses/
submission-link: https://leetcode.com/problems/generate-parentheses/submissions/965636804/
submission-link: https://leetcode.com/problems/generate-parentheses/submissions/966064297/

"""

from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        parantheses_stack = []
        res = []

        def backtrack(open_count, close_count):
            if open_count == close_count == n:
                res.append("".join(parantheses_stack))
                return

            if open_count < n:
                parantheses_stack.append('(')
                backtrack(open_count+1, close_count)
                parantheses_stack.pop()

            if close_count < open_count:
                parantheses_stack.append(')')
                backtrack(open_count, close_count+1)
                parantheses_stack.pop()

        backtrack(0, 0)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))

