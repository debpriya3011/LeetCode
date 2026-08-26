class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows ==1 or numRows>=len(s):
            return s

        emp =[""]
        emp_list = emp*numRows
        row = 0
        direction = 1
        
        for i in s:
            emp_list[row]+=i
            if row == numRows-1:
                direction = -1
            elif row == 0:
                direction = 1

            row+=direction
        return "".join(emp_list)
            
