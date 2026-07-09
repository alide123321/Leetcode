class Solution:
    def sumAndMultiply(self, n: int) -> int:

        n = str(n)
        x = "0"
        sum = 0

        for c in n:

            if c == '0': continue

            x += c
            sum += int(c)

        return int(x) * sum
        