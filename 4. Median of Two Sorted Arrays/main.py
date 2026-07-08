class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m, n = len(nums1), len(nums2)
        halfLen = math.ceil((m + n)/2)
        if (m + n) % 2 == 0:
            halfLen += 1
        lp, rp = 0, 0
        arr = []

        for i in range(halfLen):
            if lp > m-1:
                arr.append(nums2[rp])
                rp += 1
                continue

            if rp > n-1:
                arr.append(nums1[lp])
                lp += 1
                continue
            
            if nums1[lp] <= nums2[rp]:
                arr.append(nums1[lp])
                lp += 1
            else: 
                arr.append(nums2[rp])
                rp += 1
        
        if (m + n) % 2 == 1:
            return arr[-1]

        return (arr[-1] + arr[-2]) / 2.0
                