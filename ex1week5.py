# Copy from past week into a procedure.
def ln_search(V :tuple , val):
    res = ()
    for x in V:
        if x%2 == 0 and x > val:
            res = res + (x,)
    return res