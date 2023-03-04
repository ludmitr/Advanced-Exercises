"""
Write a function:

def solution(A, B, C)

that, given three unsigned 30-bit integers A, B and C, returns the number of
unsigned 30-bit integers conforming to at least one of the given integers.
https://app.codility.com/programmers/trainings/9/count_conforming_bitmasks/
"""
def count_common(positions: list):
    one_in_bin = len(positions)
    return 2**(30-one_in_bin)
def solution(a: int, b: int, c: int):
    solution_list = []


    a_list = conforming_numbers(bin(a)[2:])
    if a_list[0] == 0: return 2**30
    b_list = conforming_numbers(bin(b)[2:])
    if b_list[0] == 0: return 2 ** 30
    c_list = conforming_numbers(bin(c)[2:])
    if c_list[0] == 0: return 2 ** 30

    a_b, a_c = count_common(list(set(a_list[1] + b_list[1]))), count_common(list(set(a_list[1] + c_list[1])))
    b_c, a_b_c = count_common(list(set(b_list[1] + c_list[1]))), count_common(list(set(a_list[1] + b_list[1] + c_list[1])))
    common = a_b + ac + b_c - a_b_c
    return a_list[0] + b_list[0] + c_list[0] - common

def conforming_numbers(b_number: str) -> list:
    """

    Args:
        b_number: binary number in string

    Returns:(list). return listo of int and list. int is  amount of binary numbers 0 -
    2**30 that conform bnumber and list with indexes, each index represent position of 1 in binary number

    """

    if b_number == "0":
        return [0, []]
    b_lenghth = len(b_number)
    b_number = "0" * (30 - b_lenghth) + b_number
    one_indexes_list = []
    for x in range(len(b_number)):
        if b_number[x] == "1":  one_indexes_list.append(x)

    number_of_zeroes = 30 - len(one_indexes_list)

    return [2**number_of_zeroes, one_indexes_list]


def binary_variations_plus_one(variation_list: list):
    new_list = variation_list.copy()
    for x in [0, 1]:
        for var in variation_list:
            new_list.append(var + str(x))
    return new_list





def main():

    print(solution(1073741727, 1073741631, 1073741679))
    a = conforming_numbers(bin(1023)[2:])

if __name__ == "__main__":
    main()