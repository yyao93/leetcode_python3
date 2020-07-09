class Solution:
    def intToRoman(self, num: int) -> str:
        I2R = {0: {1: "I", 5: "V"}, 1: {1: "X", 5: "L"}, 2: {1: "C", 5: "D"}, 3: {1: "M"}}
        ret = "M" * (num // 1000)
        num %= 1000
        for i in range(2, -1, -1):
            n, num = divmod(num, 10 ** i)
            if n == 0:
                continue
            elif n < 4:
                ret += n * I2R[i][1]
            elif n == 4: 
                ret += I2R[i][1] + I2R[i][5]
            elif n < 9:
                ret += I2R[i][5] + (n - 5) * I2R[i][1]
            else:
                ret += I2R[i][1] + I2R[i + 1][1]
        return ret
