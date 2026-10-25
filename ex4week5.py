# This is done past week.
# Pre: non-empty tuple of values
# linear time
def maximum(T):
    m = T[0]
    for x in T:
        if x > m:
            m = x
    return m

# constant time
def maximum_on_sorted(T: tuple):
    return T[len(T)-1]