class Solution:
    def reverse(self, x):
        ret = 0
        while x:
            ret = ret * 10 + x % 10
            x //= 10
        return ret
