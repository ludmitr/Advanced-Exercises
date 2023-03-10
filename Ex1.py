def prime_number (prime_index:int) -> int:
    """"
    Desctiprion:
    calculate the prime number of a given index

    Parameters:
    prime_index(int): the index of a prime number to be calculated

    Returns:
    int: the prime number

    Example:
    >>> last_prime(5)
    11
    """
    prime_list = []
    current_number = 1
    while len(prime_list) != prime_index:
        if prime_check(current_number):
            prime_list.append(current_number)

        current_number += 1
    
    return prime_list[prime_index - 1]  

                
def prime_check(num:int)-> bool:
    """
    checking if this number is prime

    Parameters:
    num(int): number to check if its prime

    Returns
    True: if its a prime number
    False: if its not a prime number
    """
    is_prime = False
    if num == 1:
        return False
    if num == 2:
        return True
    if num == 3:
        return True
    # every prime number can be represented as 6n-1 or 6n+1    
    if num % 6 in [1,5]:  
        is_prime = True
        for x in range(2,int((num+2)/2) ):
                    if (num % x) == 0:
                        is_prime = False

    return is_prime


print(prime_number(100))