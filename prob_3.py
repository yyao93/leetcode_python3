class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        # sliding window
        visited = set()
        start = 0
        maxLen = 0
        for end in range(len(s)):
            if s[end] not in visited:
                visited.add(s[end])
                maxLen = max(maxLen, end - start + 1)
                continue
            visited.add(s[end])
            while s[start] != s[end]:
                visited.remove(s[start])
                start += 1
            start += 1
            maxLen = max(maxLen, end - start + 1)
        maxLen = max(maxLen, end - start + 1)
        return maxLen
