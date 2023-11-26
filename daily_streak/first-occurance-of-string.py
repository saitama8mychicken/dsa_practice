"""

"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_ind = 0
        for haystack_ind  in range(len(haystack)):
            next_haystack_ind = haystack_ind
            print(haystack_ind, needle_ind)
            while next_haystack_ind < len(haystack) and needle_ind < len(needle) and  haystack[next_haystack_ind] == needle[needle_ind]:
                 print("======>", next_haystack_ind, needle_ind)
                 next_haystack_ind += 1
                 needle_ind += 1

            if needle_ind == len(needle):
                return haystack_ind
            else:  # reset index of needle to 0 to match it again
                needle_ind = 0

        return -1



if __name__ == "__main__":
    s = Solution()
    out = s.strStr("sadbutsad", "sad")
    print(out)


