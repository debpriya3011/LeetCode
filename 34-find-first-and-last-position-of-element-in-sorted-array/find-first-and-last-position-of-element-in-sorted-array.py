class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        first = -1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                first = mid
                store = mid
                right = mid -1
                
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1

        if first == -1:
            return [-1, -1]

        left = first
        right = len(nums) -1
        last = -1

        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                last = mid
                left = mid +1
                
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1

        return [first, last]

        # count = nums.count(target)
        # first_index = nums.index(target) if count>0 else -1
        # last_index = first_index+count-1 if first_index!=-1 else -1
        # return [first_index,last_index]


