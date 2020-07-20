# Complete the highestValuePalindrome function below.
def highestValuePalindrome(s, n, k):
    if(k >= n ):
        return "9"*n
    
    s = list(s)
    k 
    middle = n//2
    changed = [False for e in range(middle + 1) ]
    for idx in range(middle):
        r_idx = middle +  idx if n%2 == 0 else middle + idx + 1
        l_idx = middle -1 - idx
    
        if s[r_idx] != s[l_idx]:
            if k == 0:
                return "-1"
            s[r_idx] = s[l_idx] = max(s[r_idx], s[l_idx])
            k = k -1
            changed[l_idx] = True
    
    
    idx_change = 0
    while(k>0 and idx_change <= middle): 
        if changed[idx_change]:
            if s[idx_change] != "9":
                s[idx_change] = s[ -idx_change -1] = "9"
                k = k -1
        
        elif not changed[idx_change]:
            if s[idx_change] != "9" and k >= 2:
                s[idx_change] = s[ -idx_change -1] = "9"
                k = k -2

        idx_change += 1

    #have 1 change left for odd          
    if k > 0:
        s[middle] = "9"


    return "".join(s)
        
        
