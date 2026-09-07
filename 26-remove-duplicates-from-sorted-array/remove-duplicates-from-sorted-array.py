class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = set(nums)
        b = len(a)
        c = list(a)
        c.sort()
        nums[:b]=c
        return b

        