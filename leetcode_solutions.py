class Solution:
    
    #https://leetcode.com/problems/generate-parentheses   
    #Dynamic programming algorithm. Faster than 99.83% of other submissions
    past_sols = dict()
    def generateParenthesis(self, n: int) -> List[str]:
     
        if n in Solution.past_sols:
            return Solution.past_sols[n]
        elif n==0:
            Solution.past_sols[n] = res = [""]
            return res
        
            
        res = []
        for idx in range(n):
            left_prev_sol = self.generateParenthesis(idx)
            right_prev_sol = self.generateParenthesis(n-idx-1)
            for sol_l in left_prev_sol:
                for sol_r in right_prev_sol:
                    to_append = "(" + sol_l + ")" +sol_r
                    res.append(to_append)
        Solution.past_sols[n] = res   
            
        return res
            
            
    
   
    #https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to
    #Faster than 99.78% of other submissions
    def groupThePeople(self, sizes: List[int]) -> List[List[int]]:
        
        sizes2groups= dict()
                
        for idx,size in enumerate(sizes):
            
            if size in sizes2groups:
                groups = sizes2groups[size] 
                if len(groups[-1]) < size:
                    groups[-1].append(idx)
                else:
                    groups.append([idx])
            
                
            else:
                sizes2groups[size] = [[idx]]
        
        res = [ group for groups in  sizes2groups.values() for group in groups ]
        return res
        
        
            
            
