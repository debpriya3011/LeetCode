class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) -1
        got = False
        while start<=end:
            mid = (start+end)//2
            if nums[mid] == target:
                got = True
                return mid
            if nums[mid]>target:
                end = mid -1
            if nums[mid]<target:
                start = mid +1
        if got is False:
            return start
        