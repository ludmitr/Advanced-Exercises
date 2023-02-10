import sympy

def truncatable_prime(num =7):
    """
    make a list of first 11 truncatable prime numbers

    Returns:
    list:  returns list of first 11  truncatable prime numbers
    """
    tprime_list = []
    while len(tprime_list) != 11:
        next_prime = sympy.nextprime(num)
        if is_trunctable(next_prime):
            tprime_list.append(next_prime)
        num = next_prime

    return tprime_list



def is_trunctable(num):
    s_number = str(num)
    is_left = True
    is_right = True
    # each loop run remove number from left and check if its prime
    for x in range(1,len(s_number)):
        if sympy.isprime(int(s_number[x:])) == False:
            is_left = False
            break
    # each loop run remove number from left and check if its prime
    for x in range(len(s_number)-1,0,-1):
        if sympy.isprime(int(s_number[:x])) == False:
            is_right = False
            break
    return is_right and is_left        

print(sum(truncatable_prime()))