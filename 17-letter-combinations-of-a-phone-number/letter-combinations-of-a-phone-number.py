class Solution:
    from itertools import product
    def letterCombinations(self, digits: str) -> List[str]:
        mapped ={"2":"abc" ,
                 "3":"def" ,
                 "4":"ghi" ,
                 "5":"jkl",
                 "6":"mno" ,
                 "7":"pqrs" ,
                 "8":"tuv" ,
                 "9":"wxyz" ,
                 }

        my_list =[mapped[i] for i in digits]

        return ["".join(p) for p in product(*my_list)]
     
        