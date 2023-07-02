"""

"""

class Solution:
    def count_no_of_distinct_anagram(self, str_):
        total_anagrams = set()

        def backtrack(str_available, path):
            print(str_available, path)
            if len(str_available) == 0:
                total_anagrams.add("".join(path))
                return

            else:
                for ind in range(len(str_available)):
                    backtrack(str_available[:ind] + str_available[ind+1:], path+[str_available[ind]])

        backtrack(str_, [])

        return len(total_anagrams)

    def countAnagrams(self, s: str) -> int:
        count_of_anagrams = 1

        for str_ in s.split(" "):
            count_of_anagrams *= self.count_no_of_distinct_anagram(str_)


        return count_of_anagrams



if __name__ == "__main__":
    s = Solution()
    print(s.countAnagrams("act cat tac god dog"))

