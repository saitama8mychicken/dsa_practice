"""

Print all duplicates in a input string

"""


class Solution:

    def print_all_duplicates(self, input_string):

        char_dict = {}
        for char in input_string:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

        for char, count in char_dict.items():
            if count > 1:
                print(char, count, end=" ")


if __name__ == "__main__":
    s = Solution()
    input_string = "geeksforgeeks"
    s.print_all_duplicates(input_string)