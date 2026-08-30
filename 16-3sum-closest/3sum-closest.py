class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        a = len(nums)
        if a == 3:
            return sum(nums)
        nums.sort()
        index = 0
        closest = nums[0]+nums[1]+nums[2]
        for i in range(a-2):
            left = i + 1
            right = a - 1
            while left<right:
                total = nums[i]+nums[left]+nums[right]
                c = abs(total - target)
                d = abs(closest - target)
                if c<d:
                    closest = total  
                if total>target:
                    right-=1
                elif total<target:
                    left+=1
                else:
                    return total
        return closest




