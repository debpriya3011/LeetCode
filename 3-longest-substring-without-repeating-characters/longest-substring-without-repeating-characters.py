class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            seen = set()
            for j in range(i,len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
            c = len(seen)
            count = c if count<c else count
        return count
        