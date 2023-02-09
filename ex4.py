def factorial(num:int)-> int:
    """
    
    """
    if  num ==1:
        return num*1

    num *= factorial(num-1)

    return num
def count_number(num:int)->int:
    number_list = [int(number) for number in str(num)]
    sum = 0
    for x in number_list:
        sum += x
    return sum    



print(count_number(factorial(100)))