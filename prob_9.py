class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        flip = 0
        origin = x
        while x:
            flip = flip * 10 + x % 10
            x //= 10
        return origin == flip
