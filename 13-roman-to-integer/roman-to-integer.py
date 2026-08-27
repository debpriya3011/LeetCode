class Solution:
    new_dict ={
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    def romanToInt(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and self.new_dict[s[i]] < self.new_dict[s[i+1]]:
                result -= self.new_dict[s[i]]
            else:
                result += self.new_dict[s[i]]

            
        return result

        
        