"""
2042. Check if Numbers Are Ascending in a Sentence

A sentence is a list of tokens separated by a single space with no leading or trailing spaces. Every token is either a positive number consisting of digits 0-9 with no leading zeros, or a word consisting of lowercase English letters.

For example, "a puppy has 2 eyes 4 legs" is a sentence with seven tokens: "2" and "4" are numbers and the other tokens such as "puppy" are words.
Given a string s representing a sentence, you need to check if all the numbers in s are strictly increasing from left to right (i.e., other than the last number, each number is strictly smaller than the number on its right in s).

Return true if so, or false otherwise.


"""


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        last_number = None
        for word in s.split(" "):
            if word.isdigit():
                if last_number and int(word) <= int(last_number):
                    return False
                else:
                    last_number = word

        return True







