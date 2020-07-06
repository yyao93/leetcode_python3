class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1:
            return s
        # space complexity O(1)
        ret = ""
        for idx in range(numRows):
            cur = idx
            while cur < len(s):
                ret += s[cur]
                if idx not in {0, numRows - 1} and cur + 2 * (numRows - 1 - idx) < len(s):
                    ret += s[cur + 2 * (numRows - 1 - idx)]
                cur += 2 * (numRows - 1)
        return ret

class Solution0:
    def convert(self, s: str, numRows: int) -> str:
        ret = [""] * numRows
        idx = list(range(numRows)) + list(range(numRows - 2, 0, -1))
        for i, c in enumerate(s):
            ret[idx[i % len(idx)]] += c
        return "".join(ret)
