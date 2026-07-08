import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        pattern = ""
        lenP = len(p)

        for i in range(lenP):
            if i + 1 < lenP and p[i + 1] == "*":

                pattern += ".*" if p[i] == "." else "(" + p[i] + ")*"
                i +=1
            else:
                pattern += p[i]

        return re.compile(pattern).match(s)