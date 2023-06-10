"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.


Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23


question-link: https://leetcode.com/problems/koko-eating-bananas/description/
submission-link: https://leetcode.com/problems/koko-eating-bananas/submissions/967533824/
"""

from typing import List


class Solution:

    def calculate_time_taken_to_eat_pile(self, piles: List[int], per_hour_count: int) -> int:
        total_time_taken = 0
        for pile in piles:
            perfect_divide = pile//per_hour_count
            reminder = pile % per_hour_count
            total_time_taken += perfect_divide

            if reminder:
                total_time_taken += 1

        return total_time_taken

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_pile = min(piles)//h
        min_pile = min_pile if min_pile >0 else 1
        max_pile = max(piles)
        for eating_speed in range(min_pile, max_pile+1):
            print("Trying with =>>>>>", eating_speed)
            time_taken = self.calculate_time_taken_to_eat_pile(piles, eating_speed)
            if time_taken <= h:
                return eating_speed

        return 0


if __name__ == "__main__":
    s = Solution()
    print(s.minEatingSpeed([312884470], 312884469))
