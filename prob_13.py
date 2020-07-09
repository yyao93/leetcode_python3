class Solution:
    def romanToInt(self, s: str) -> int:
        R2I = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ret = R2I[s[-1]]
        for i in range(len(s) - 1):
            if R2I[s[i]] < R2I[s[i + 1]]:
                ret -= R2I[s[i]]
            else:
                ret += R2I[s[i]]
        return ret
