"""

"""
from typing import List


class Solution:

    def __init__(self):
        self.permutated_results = []

    def check_if_positions_are_valid(self, positions):
        """
        check if positions are valid
        Args:
            positions:

        Returns: True if valid, False otherwise
        """
        # check for linearity => this will never be the case since tey were initially rearanged
        # check for cross pattern
        positive_diagonal_set = set()
        negative_diagonal_set = set()

        for row_ind, row in enumerate(positions):
            position_of_q = row.find('Q')
            positive_diagonal = row_ind + position_of_q
            negative_diagonal = row_ind - position_of_q

            if positive_diagonal in positive_diagonal_set or negative_diagonal in negative_diagonal_set:
                return False
            else:
                positive_diagonal_set.add(positive_diagonal)
                negative_diagonal_set.add(negative_diagonal)

        return True

    def backtrack(self, nums, path):

        if len(nums) == 0:
            self.permutated_results.append(path)

        for i in range(len(nums)):
            if self.check_if_positions_are_valid(path + [nums[i]]) is False:
                continue
            self.backtrack(nums[:i] + nums[i + 1:], path + [nums[i]])

    def solveNQueens(self, n: int) -> List[List[str]]:

        possible_sequences = []

        for i in range(n):
            sequence = "." * i + "Q" + "." * (n - i - 1)
            possible_sequences.append(sequence)

        self.backtrack(possible_sequences, [])

        possible_positions = self.permutated_results

        return possible_positions


if __name__ == "__main__":
    s = Solution()
    print(s.solveNQueens(4))
