class Solution:
    def longestPalindrome(self, s: str) -> str:
        long = ""
        for i in range(len(s)):
            left = i
            right = i
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    left-=1
                    right+=1
                else:
                    break
            palindrome = s[left+1:right]
            if len(long)<len(palindrome):
                long = palindrome

            left = i
            right = i+1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    left-=1
                    right+=1
                else:
                    break
            palindrome = s[left+1:right]
            if len(long)<len(palindrome):
                long = palindrome



        return long


        