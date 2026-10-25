# Mind T is non_empty sorted tuple
# of integers
# This is very important!!! 
def mode(T: tuple):
    n,mode,frec,tmp = 1,T[0],1,1
    while n < len(T):
        tmp = (tmp + 1) if T[n]==T[n-1] else 1
        if tmp > frec:
            mode,frec = T[n],tmp
        n = n + 1
    return mode,frec
        