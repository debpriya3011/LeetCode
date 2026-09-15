class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrace(start,target,current):
            if target == 0:
                result.append(current.copy())
                return
            for i in range(start,len(candidates)):
                num = candidates[i]
                if num>target:
                    break
                current.append(num)
                backtrace(i,target-num,current)
                current.pop()
        backtrace(0,target,[])
        return result
        