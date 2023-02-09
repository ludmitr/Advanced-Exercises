def list_prime (prime_index:int) -> int:
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
    prime_list = [1,2]
    highest_prime = 2
    if prime_index == 1:
        return prime_list[0]
    elif prime_index == 2:
        return prime_list[1]
    else:
        while len(prime_list) == prime_index:
            highest_prime +=1
            is_prime = True
            for x in range(2,int((highest_prime+1)/2) ):
                if (highest_prime % x) == 0:
                    is_prime = False
            if is_prime:
                prime_list.append(highest_prime)
                # if highest_prime % x != 0
                
def prime_check(num:int)-> bool:
    """
    checking if this number is prime

    Parameters:
    num(int): number to check if its prime

    Returns
    True: if its a prime number
    False: if its not a prime number
    """
    is_prime = True
    
    for x in range(2,int((num+2)/2) ):
                if (num % x) == 0:
                    is_prime = False

    return is_prime


print(prime_check())