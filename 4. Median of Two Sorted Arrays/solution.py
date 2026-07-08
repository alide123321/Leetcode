from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array for O(log(min(m,n))) binary search
        A, B = nums1, nums2
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m

        imin, imax, half = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half - i

            if i < m and j > 0 and B[j - 1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and j < n and A[i - 1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect
                if i == 0:
                    max_left = B[j - 1]
                elif j == 0:
                    max_left = A[i - 1]
                else:
                    max_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return float(max_left)

                if i == m:
                    min_right = B[j]
                elif j == n:
                    min_right = A[i]
                else:
                    min_right = min(A[i], B[j])

                return (max_left + min_right) / 2.0

                