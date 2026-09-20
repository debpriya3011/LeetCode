class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        from itertools import permutations
        a = set(permutations(nums))
        print(a)
        b = [list(i) for i in a]
        return b
        # a = permutations(nums)
        # b = []
        # for i in a :
        #     if list(i) not in b:
        #         b.append(list(i))
    