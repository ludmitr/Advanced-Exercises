def list_prime (prime_index:int) -> int:
    
    if prime_index == 1:
        return 2
    elif prime_index == 2:
        return 3
    else:
        prime_index -=2
        if (prime_index % 2 ) != 0:
            return 6*prime_index -1
        else:
            return 6*prime_index +1



print(list_prime(10001))