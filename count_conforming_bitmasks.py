"""
Write a function:

def solution(A, B, C)

that, given three unsigned 30-bit integers A, B and C, returns the number of
unsigned 30-bit integers conforming to at least one of the given integers.
https://app.codility.com/programmers/trainings/9/count_conforming_bitmasks/
"""
def count_common(positions: list):
    """
    Calculate amount of binary numbers that conform  binary number with 1 positions in list
        positions: list with integers, each integer is position of 1 in binary number 2**30
    Returns: amount of binary numbers that conform  binary number with 1 positions in list

    """
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

    #  instead of bitwise, using list of indexes that represents positions of 1 in binary number.
    # instead of a|b  i combine list of a and b and remove duplicates by tranforming it to set and back to list
    a_b, a_c = count_common(list(set(a_list[1] + b_list[1]))), count_common(list(set(a_list[1] + c_list[1])))
    b_c, a_b_c = count_common(list(set(b_list[1] + c_list[1]))), count_common(list(set(a_list[1] + b_list[1] + c_list[1])))
    common = a_b + a_c + b_c - a_b_c
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
    b_length = len(b_number)
    # adding zeroes to the left of the number to match 2**30
    b_number = "0" * (30 - b_length) + b_number
    one_indexes_list = []
    # saving positions of 1 in binary number to use it later to to remove duplicates
    for x in range(len(b_number)):
        if b_number[x] == "1":  one_indexes_list.append(x)

    number_of_zeroes = 30 - len(one_indexes_list)
    # counting all groups 2 ** 30-len(one_indexes_list) that conform current b_number
    return [2**number_of_zeroes, one_indexes_list]


def main():
    print(solution(1023, 8184, 65472))


if __name__ == "__main__":
    main()
