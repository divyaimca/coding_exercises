from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = sorted(nums1 + nums2)
        if len(l1) % 2 == 0:
            return (l1[len(l1)//2]+l1[(len(l1)//2)-1])/2
        else:
            return l1[(len(l1)//2)] 

print(Solution().findMedianSortedArrays([1,2],[3,4]))

print(Solution().findMedianSortedArrays([1],[3,4]))