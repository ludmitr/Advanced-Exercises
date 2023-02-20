# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
import sympy


def find_exception() -> int:
    oddcomp_nums = [4,6,8,9,10]
    while True:
        check_num = oddcomp_nums[-1]
        if is_exception(check_num):
            return check_num
        check_num += 1
        while not is_odd_and_composite(check_num):
            check_num+=1
        oddcomp_nums.append(check_num)

def is_odd_and_composite(n):
    if n ==1:
        return False
    if n % 2 == 0:
        return False
    if sympy.isprime(n):
        return False
    return True
def is_exception(check_num:int)-> bool:
    is_num = True
    prime_list = [2,3,5,7,11]
    for prime in prime_list:
            
            num_square = 1
            while (prime +2 * num_square**2) <= check_num:
                if (prime +2 * num_square**2) == check_num:
                    return False
                else:
                    num_square+=1
            if prime == prime_list[-1] and prime < check_num:
                prime_list.append(sympy.nextprime(prime))
    return is_num



print(find_exception())