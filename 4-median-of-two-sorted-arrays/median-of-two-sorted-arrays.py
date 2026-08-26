class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_list = nums1+nums2
        import numpy
        return numpy.median(new_list)
        