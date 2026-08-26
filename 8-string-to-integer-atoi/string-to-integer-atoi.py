class Solution:
    import re
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        pattern = r"[-+]?\d+"
        a = re.match(pattern,s)
        if not a:
            return 0
        b = a.group()
        sign = 1
        i = 0
        if b[0] == "-":
            sign = -1
            i+=1
        if b[0] == "+":
            i+=1
        num = 0
        while i<len(b):
            num = num * 10 + (ord(b[i])-ord('0'))
            i+=1

        if sign * num < -2147483648:
            return -2147483648

        if sign * num > 2147483647:
            return 2147483647

        return sign * num
        
        


        