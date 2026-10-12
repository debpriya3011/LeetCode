class Solution:
    from itertools import permutations
    def permute(self, nums: list[int]) -> list[list[int]]:
        return list(permutations(nums))
        