class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = (dividend<0)!=(divisor<0)
        dividend = abs(dividend)
        divisor = abs (divisor)
        quotient = 0

        while dividend>=divisor:
            temp = divisor
            count = 1
            while dividend >= temp + temp:
                temp +=temp
                count +=count
            dividend -=temp
            quotient+=count
        if negative:
            quotient = -quotient
        if quotient < -(2**31):
            return -(2**31)

        if quotient > 2**31 - 1:
            return 2**31 - 1
        return quotient



        