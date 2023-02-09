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
    binom_k = x
    return math.comb(binom_n,binom_k)



print(lathice_path(20,20))