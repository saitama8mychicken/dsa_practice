"""

Valid Parantheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true


"""

class Solution:
    def __init__(self):
        self.opening_parantheses = set(['(', '[', '{'])
        self.closing_parantheses = set([')', ']', '}'])
    
    def type_of_parantheses(self, parantheses):
        if parantheses in self.opening_parantheses:
            return "opening"
        elif parantheses in self.closing_parantheses:
            return "closing"

    def reverse_parantheses(self, parantheses):
        if parantheses == "(":
            return ")"
        elif parantheses == "[":
            return "]"
        elif parantheses == "{":
            return "}"
        else:
            return None

    def isValid(self, s: str) -> bool:
        
        parantheses_order = []

        for parantheses in s:
            # print(parantheses, parantheses_order)
            if self.type_of_parantheses(parantheses) == "opening":
                parantheses_order.append(parantheses)

            elif self.type_of_parantheses(parantheses) == "closing":
                if len(parantheses_order) == 0:
                    return False

                if self.reverse_parantheses(parantheses_order[-1]) == parantheses:
                    parantheses_order = parantheses_order[:-1]
                else:
                    return False

        if len(parantheses_order) > 0:
            return False
        else:
            return True


