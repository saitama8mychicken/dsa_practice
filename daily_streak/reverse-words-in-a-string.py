"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.



Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.


Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

question-link: https://leetcode.com/problems/reverse-words-in-a-string/description/
submission-link: https://leetcode.com/problems/reverse-words-in-a-string/submissions/966722968/

"""


class Solution:
    def reverseWords(self, s: str) -> str:

        reversed_string = ""
        last_word = None

        for i in range(len(s)):
            index_from_last = len(s) - i - 1
            current_char = s[index_from_last]

            if current_char == " ":
                if last_word is not None:
                    reversed_string += last_word
                    reversed_string += ' '
                    last_word = None

            else:
                if last_word is None:
                    last_word = current_char
                else:
                    last_word = current_char + last_word

                if index_from_last == 0:
                    reversed_string += last_word

            # finally there could be a extra space being added by above , lets remove that
        if reversed_string[-1] == " ":
            reversed_string = reversed_string[:-1]

        return reversed_string


if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords("  hello update me with this  "))