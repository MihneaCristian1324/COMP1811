# Hard
# Tuple possible empty, return tuple of position
def cool_numbers(T):
    res = ()
    sum = T[0] + T[1]
    n = 2  
    
    while n < len(T):
        if T[n] == sum:
            res = res + (n,)  
        
        sum = sum + T[n]
        n = n + 1
        
    return res

