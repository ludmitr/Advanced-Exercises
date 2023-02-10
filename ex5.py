import sympy
tprime_list = []
def truncatable_prime(num):
    pass
def is_trunctable(num):
    s_number = str(num)
    is_left = True
    is_right = True

    for x in range(1,len(s_number)):
        if sympy.isprime(int(s_number[x:])) == False:
            is_left = False
            break
    for x in range(len(s_number)-1,0,-1):
        if sympy.isprime(int(s_number[:x])) == False:
            is_right = False
            break
    return is_right and is_left        

print(is_trunctable())