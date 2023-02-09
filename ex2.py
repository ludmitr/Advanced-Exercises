import math

def lathice_path(x:int,y:int):
    """
    function that will return number of paths

    Parameters:
    x(int): represent x position of a point
    y(int): represent y position of a point

    Returns
    count(int): number of path to reach (x,y) point avaible
    
    """
    binom_n = x+y
    binom_k = 2

    if binom_k == 1 or y == binom_n:
        return(1)

    if binom_k > binom_n:
        return(0)        
    else:
        a = math.factorial(binom_n)
        b = math.factorial(binom_k)
        div = a // (b*(binom_n-binom_k))
        return(div) 

print(lathice_path(5,5))