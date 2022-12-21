import itertools
import timeit


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = 0
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        # for i in range(len(s)-1, -1, -1):
        i = len(s) - 1
        while i >= 0:
            int_num = roman_to_int[s[i]]
            if (s[i] == 'V' or s[i] == 'X') and s[i-1] == 'I' and i > 0:
                roman += int_num - 1
                i -= 2
            elif (s[i] == 'L' or s[i] == 'C') and s[i-1] == 'X' and i > 0:
                roman += int_num - 10
                i -= 2
            elif (s[i] == 'D' or s[i] == 'M') and s[i-1] == 'C' and i > 0:
                roman += int_num - 100
                i -= 2
            else:
                roman += int_num
                i -= 1
        return roman


if __name__ == '__main__':
    s = Solution()
    start = timeit.default_timer()
    print(s.romanToInt("MMMCDXC"))
    end = timeit.default_timer()
    print(end - start)
