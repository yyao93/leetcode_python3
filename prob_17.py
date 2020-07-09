class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        ret = []
        def dfs(idx, path):
            if idx == len(digits):
                if path:
                    ret.append(path) 
                return
            nonlocal letters
            for l in letters[digits[idx]]:
                dfs(idx + 1, path + l)
        dfs(0, "")
        return ret
