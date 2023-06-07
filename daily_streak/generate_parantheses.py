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


"""

from typing import List


class Solution:

    def generate_next_parantheses(self, parantheses_list, n):
        count_opening_parantheses = parantheses_list.count('(')
        count_closing_parantheses = parantheses_list.count(')')
        parantheses_score = count_opening_parantheses - count_closing_parantheses

        if parantheses_score > 0:
            if count_opening_parantheses < n:
                return ['(', ')']
            elif count_closing_parantheses < n:
                return [')']
            else:
                return None
        elif parantheses_score == 0:
            if count_opening_parantheses < n:
                return ['(']
            else:
                return None

    def generateParenthesis(self, n: int) -> List[str]:
        possible_parantheses = []

        # start having parantheses
        if n > 0:
            possible_parantheses = [
                ['(']
            ]

        i = 0
        while True:
            current = possible_parantheses[i]
            next_parantheses = self.generate_next_parantheses(current, n)
            print(next_parantheses)
            if next_parantheses:
                if len(next_parantheses) > 1:
                    current_copy = list(current)
                    current.append(next_parantheses[0])
                    current_copy.append(next_parantheses[1])
                    possible_parantheses.append(current_copy)
                elif len(next_parantheses) == 1:
                    current.append(next_parantheses[0])

            else:
                i += 1
                if i >= len(possible_parantheses):
                    break
        possible_parantheses = [''.join(parantheses) for parantheses in possible_parantheses]
        return possible_parantheses


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))