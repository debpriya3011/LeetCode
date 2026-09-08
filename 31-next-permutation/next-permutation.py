class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = -1
        a = len(nums)-2
        for i in range(a,-1,-1):
            if nums[i] < nums[i+1]:
                pivot = i
                break
        if pivot!=-1:
            for j in range(a+1,i,-1):
                if nums[j]>nums[pivot]:
                    nums[j],nums[pivot] =nums[pivot],nums[j]
                    break
        start = pivot + 1
        end = a + 2
        new_list = sorted(nums[start:end])
        nums[start:end] = new_list



        