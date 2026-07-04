import math

class Solution:
    def kthFactor(self, n: int, k: int) -> int:

        kCounter = 0

        for i in range(1, n+1):

            if math.fmod(n,i) == 0:
                kCounter += 1
                
                if kCounter == k:
                    return i

        return -1