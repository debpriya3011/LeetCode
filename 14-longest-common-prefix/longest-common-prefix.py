class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = min(len(i) for i in strs)
        start = 0
        end = a
        result = ""
        while start<end:
            mid = (start+end+1)//2
            if len(set(i[:mid] for i in strs)) == 1:
                result = strs[0][:mid]
                start = mid 
            else:
                end = mid - 1
        return result
            
        