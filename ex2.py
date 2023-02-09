import math

def lathice_path(x:int,y:int):
    """
    recursive function that will return number of paths

    Parameters:
    x(int): represent x position of a point
    y(int): represent y position of a point

    Returns
    count(int): number of path to reach (x,y) point avaible
    
    """


    if y == 1 or y == x:
        return(1)

    if y > x:
        return(0)        
    else:
        a = math.factorial(x)
        b = math.factorial(y)
        div = a // (b*(x-y))
        return(div) 

print(lathice_path(2,2))