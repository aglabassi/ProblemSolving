class Solution:
    #https://leetcode.com/problems/generate-parentheses
    
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:
            return [""]
        
        res = []
        
        for idx in range(n):
            left_prev_sol = self.generateParenthesis(idx)
            right_prev_sol = self.generateParenthesis(n-idx-1)
            for sol_l in left_prev_sol:
                for sol_r in right_prev_sol:
                    to_append = "(" + sol_l + ")" +sol_r
                    res.append(to_append)
           
            
        return res
            
            
