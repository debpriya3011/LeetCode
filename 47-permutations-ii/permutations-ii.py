class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        from itertools import permutations
        a = permutations(nums)
        b = []
        for i in a :
            if list(i) not in b:
                b.append(list(i))
        return b
        