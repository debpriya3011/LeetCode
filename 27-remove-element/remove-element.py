class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        filtered_list = [i for i in nums if i!=val]
        a = len(filtered_list)
        nums[:a] = filtered_list
        return a
        