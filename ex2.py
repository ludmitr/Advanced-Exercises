def lathice_path(x:int,y:int):
    """
    recursive function that will return number of paths

    Parameters:
    x(int): represent x position of a point
    y(int): represent y position of a point

    Returns
    count(int): number of path to reach (x,y) point avaible
    
    """
    if x == 0 and y == 0:
        return 1

    count = 0

    if x > 0:
        count += lathice_path(x-1,y)
    if y > 0:
        count += lathice_path(x,y-1) 
    
    return count