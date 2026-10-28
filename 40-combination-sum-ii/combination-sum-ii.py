class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        mainb = []
        candidates.sort()
        def backtrace(start,c,d):
            if d == 0:
                mainb.append(list(c))
                return

            for j in range(start,len(candidates)):
                if j>start and candidates[j] == candidates[j-1]:
                    continue

                if candidates[j]>d:
                    break

                c.append(candidates[j])
                backtrace(j+1,c,d-candidates[j])
                c.pop()
        backtrace(0,[],target)
        return mainb







