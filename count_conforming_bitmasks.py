"""
Write a function:

def solution(A, B, C)

that, given three unsigned 30-bit integers A, B and C, returns the number of
unsigned 30-bit integers conforming to at least one of the given integers.
https://app.codility.com/programmers/trainings/9/count_conforming_bitmasks/
"""


def solution(a: int, b: int, c: int):
    conforming_list_a = conforming_numbers(bin(a)[2:])
    conforming_list_b = conforming_numbers(bin(b)[2:])
    conforming_list_c = conforming_numbers(bin(c)[2:])

    # merging lists together and removing duplicates
    merged_list = conforming_list_a + conforming_list_b + conforming_list_c
    merged_list = list(set(merged_list))

    return merged_list
def conforming_numbers(b_number: str) -> list:
    """
    function counts all possible binary numbers that conforming b_number
    Args:
        b_number: (str)

    Returns: list of all possible binary numbers that conforming b_number. each element in list is a string

    """
    zero_indexes_list = []
    conforming_list = []
    # creating list where each element is original index of 0 in b_number
    for x in range(len(b_number)):
        if b_number[x] == "0": zero_indexes_list.append(x)

    variations_list = create_binary_variations(len(zero_indexes_list))
    # creating list of binary numbers that conform b_number
    for list in variations_list:
        counter = 0
        temp_number = b_number
        # creating new binary number using saved indexes for each 0 in bnumber
        for index in zero_indexes_list:
            temp_number = temp_number[:index] + str(list[counter]) + temp_number[index+1:]
            counter += 1
        conforming_list.append(temp_number)
    return conforming_list


def binary_variations_plus_one(variation_list: list):
    new_list = variation_list.copy()
    for x in [0, 1]:
        for var in variation_list:
            new_list.append(var + str(x))
    return new_list


def create_binary_variations(num):
    """
    Generate all possible variation for a group of variables when each variable can be 0 or 1.
    Length of the group defined by Parameter: num

    Returns:(list) each element of list is list of integers that represent one case of variation

    """
    main_list = []
    for i in range(0, 2 ** num):
        binary_string = format(i, '0{}b'.format(num))
        new_list = [int(bit) for bit in binary_string]
        main_list.append(new_list)

    return main_list


def main():
    a = 1073741727
    b = 1073741631
    c = 1073741679
    total = solution(a, b, c)
    print(total)
    print(f"the number is : {len(total)}")


if __name__ == "__main__":
    main()