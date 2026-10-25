# Pre : V possibly empty
def is_sorted(V : tuple) -> bool :
    n = 1
    while n < len(V):
        if V[n] < V[n-1]:
            return False
        n += 1
    return True


