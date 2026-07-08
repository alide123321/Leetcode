class Solution:
    def climbStairs(self, n: int) -> int:

        mem = {}

        def rec(n):

            if n in mem: return mem[n]

            if n == 0: return 1
            if n < 0: return 0

            mem[n] = rec(n-1) + rec(n-2)

            return mem[n]

        return rec(n)
