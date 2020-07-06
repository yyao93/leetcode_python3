class Solution:
    def longestPalindrome(self, string: str) -> str:
        # O(1) storage using binary
        # initialize
        prev_1 = 2 ** (len(string)) - 1
        max_len, max_s, max_e = 1, 0, 0
        prev_2 = 0
        for i in range(len(string) - 1):
            prev_2 <<= 1
            if string[i] == string[i + 1]:
                prev_2 += 1
                max_len, max_s, max_e = 2, i, i + 1
        # iteration
        for i in range(2, len(string)):
            cur, idx = 0, 2 ** (len(string) - i - 1)
            for s in range(len(string) - i):
                cur <<= 1
                if string[s] == string[s + i] and (prev_1 & (idx << 1)):
                    cur += 1
                    if i + 1 > max_len:
                        max_len, max_s, max_e = i, s, s + i
                idx >>= 1
            prev_1, prev_2 = prev_2, cur
        return string[max_s: max_e + 1]


class Solution0:
    def longestPalindrome(self, string: str) -> str:
        # If not use binary: O(n) storage
        prev_1 = [True] * len(string)
        prev_2 = [string[i] == string[i + 1] for i in range(len(string) - 1)]
        max_len, max_s, max_e = 1, 0, 0
        if any(prev_2):
            max_len, max_s = 2, prev_2.index(True)
            max_e = max_s + 1
        for i in range(2, len(string)):
            cur = []
            for s in range(len(string) - i):
                if string[s] == string[s + i] and prev_1[s + 1]:
                    cur.append(True)
                    if i + 1 > max_len:
                        max_len, max_s, max_e = i, s, s + i
                else:
                    cur.append(False)
            prev_1 = prev_2.copy()
            prev_2 = cur.copy()
        return string[max_s: max_e + 1]
