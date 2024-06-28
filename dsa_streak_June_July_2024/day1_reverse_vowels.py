class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        s = list(s)
        ptr1 = 0
        ptr2 = len(s) -1

        while ptr1 < ptr2:
            if s[ptr1].lower() not in vowels:
                ptr1 += 1
            if s[ptr2].lower() not in vowels:
                ptr2 -= 1

            if s[ptr1].lower() in vowels and s[ptr2].lower() in vowels:
                s[ptr1], s[ptr2] = s[ptr2], s[ptr1]
                ptr1 += 1
                ptr2 -= 1

        return "".join(s)
