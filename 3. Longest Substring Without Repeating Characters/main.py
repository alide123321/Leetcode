class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        letters = set()
        lp, rp, maxLength = 0, 0, 0

        for i in range(len(s)):
            while s[rp] in letters:
                letters.remove(s[lp])
                lp += 1
            
            letters.add(s[rp])
            maxLength = max(maxLength, rp - lp + 1)
            rp +=1

        return maxLength