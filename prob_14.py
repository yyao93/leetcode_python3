class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def common(i, j, c):
            tmp = min(c + 1, len(strs[i]), len(strs[j]))
            idx = 0
            while idx < tmp and strs[i][idx] == strs[j][idx]:
                idx += 1
            return idx - 1
        ret = 2 ** 31
        for i in range(len(strs) - 1):
            ret = common(i, i + 1, ret)
        return strs[0][:ret + 1] if strs else ""
