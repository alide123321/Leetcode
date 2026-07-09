class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:

        # takes too long and doesnt run.

        output = []
        modNum = 10**9 + 7
                
        def solve(n):
            x = 0
            sum = 0

            for c in n:

                if c == '0': continue

                digit = int(c)

                x = (x*10) + digit
                sum += digit

            return (x * sum) % modNum

        for q in queries:
            print(s[q[0]: q[1] +1])
            output.append(solve(s[q[0]: q[1] + 1]))

        return output