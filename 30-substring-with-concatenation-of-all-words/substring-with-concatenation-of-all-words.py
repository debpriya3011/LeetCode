class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        a = len(words)
        b = len(words[0])
        c = a*b
        result =[]
        for i in range(len(s)-c+1):
            d = s[i:i+c]
            parts = []
            for j in range(0,c,b):
                parts.append(d[j:j+b])

            if sorted(words) == sorted(parts):
                result.append(i)
        return result




        