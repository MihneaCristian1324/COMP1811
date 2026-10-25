# Copy from past week
# def int_div(a , b):
def int_div(a : int , b : int) -> tuple:
    q = 0
    r = a
    while r >= b:
        r = r - b
        q = q + 1
    return (q,r)
    