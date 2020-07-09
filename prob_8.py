class Solution:
    def myAtoi(self, s):
        sign = 1
        isSign = False
        isStart = False
        num = 0
        for c in s:
            if c == " ":
                if isStart or isSign:
                    break
                continue
            if c.isalpha() or (c in {"-", "+"} and isSign):
                break
            if c in {"-", "+"} and not isSign and not isStart:
                isSign = True
                if c == "-":
                    sign = -1
                continue
            if c.isnumeric():
                isStart = True
                num = num * 10 + int(c)
            else:
                break
        num *= sign
        return - 2 ** 31 if num <= - 2 ** 31 else 2 ** 31 - 1 if num >= 2 ** 31 - 1 else num
