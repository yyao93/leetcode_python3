class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def match(p1, p2):
            #print(s[p1:], p[p2:])
            if p1 == len(s) and p2 == len(p):
                return True
            #if p1 == len(s) or p2 == len(s):
            #   return False
            if p2 + 1 < len(p) and p[p2 + 1] == "*":
                if p[p2] != ".":
                    tmp = match(p1, p2 + 2)
                    while p1 < len(s) and s[p1] == p[p2]:
                        p1 += 1
                        tmp = tmp or match(p1, p2 + 2)
                    return tmp
                else:
                    return any(match(i, p2 + 2) for i in range(p1, len(s) + 1))
            else:
                if p1 < len(s) and p2 < len(p):
                    return (s[p1] == p[p2] or p[p2] == ".") and match(p1 + 1, p2 + 1)
                else:
                    return False
        return match(0, 0)
