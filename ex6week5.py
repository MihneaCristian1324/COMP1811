# Pre : possibly empty
def mirror(T: tuple):
    res = ()
    n = len(T) - 1 
    
    while n >= 0:
        res = res + (T[n],)  
        n = n - 1            
        
    return res