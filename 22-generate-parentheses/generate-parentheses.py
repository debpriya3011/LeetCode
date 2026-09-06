class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result =[]

        def backtrace(s,open,close):
            if len(s) ==2*n:
                result.append(s)
                return
            if open<n:
                backtrace(s+"(",open+1,close)
            if open>close:
                backtrace(s+")",open,close+1)
            
        backtrace("",0,0)
        return result
        