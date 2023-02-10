def factorial(num:int)-> int:
    """
    Calculate factorial of num
    
    Returns:
    num(int): calculated factorial
    """
    if  num ==1:
        return num*1

    num *= factorial(num-1)

    return num
def count_number(num:int)->int:
    """
    Calculating the sum of each character in num

    Returns:
    sum(int)  calculated number of a num

    
    Example:
    >>> count_number(22)
    4
    """
    number_list = [int(number) for number in str(num)]
    sum = 0
    for x in number_list:
        sum += x
    return sum    



print(count_number(factorial(100)))