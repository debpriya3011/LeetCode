class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        a = len(nums)
        index = 0
        new_sum_list = []
        for index in range(a-3):
            l1 = index
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            for l2 in range(l1+1,a-2):
                if l2 > l1 + 1 and nums[l2] == nums[l2 - 1]:
                    continue
                l3 = l2+1
                r1 = a-1

                while l3<r1:
                    new_sum = nums[l1]+nums[l2]+nums[r1]+nums[l3]
                    if new_sum == target:
                        new_sum_list.append(list((nums[l1],nums[l2],nums[l3],nums[r1])))
                        while l3 < r1 and nums[l3] == nums[l3 + 1]:
                            l3 += 1
                        while l3 < r1 and nums[r1] == nums[r1 - 1]:
                            r1 -= 1
                        l3+=1
                        r1-=1
                    elif new_sum<target:
                        l3+=1
                    elif new_sum>target:
                        r1-=1
            
        return new_sum_list



        