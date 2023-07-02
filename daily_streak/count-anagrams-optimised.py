"""

"""

class Solution:
    def count_no_of_distinct_anagram(self, str_):
        """
            Total anagrams = n! / (a! * b! * c! * d! * ...)

            where a, b, c, d are the count of each distinct character in the string
            and n is the length of the string
        """

        def factorial(num):
            if num == 0:
                return 1
            else:
                return num * factorial(num-1)

        count_of_str = {}
        for i in str_:
            if i in count_of_str:
                count_of_str[i] += 1
            else:
                count_of_str[i] = 1

        total_anagrams = factorial(len(str_))
        for key, value in count_of_str.items():
            total_anagrams = total_anagrams / factorial(value)

        return total_anagrams

    def countAnagrams(self, s: str) -> int:
        count_of_anagrams = 1

        for str_ in s.split(" "):
            count_of_anagrams *= self.count_no_of_distinct_anagram(str_)


        return count_of_anagrams



if __name__ == "__main__":
    s = Solution()
    # print(s.count_no_of_distinct_anagram("act"))
    print(s.countAnagrams("zrztwlolvcyumcsq"))
    print(s.countAnagrams("b okzojaporykbmq tybq zrztwlolvcyumcsq jjuowpp"))

