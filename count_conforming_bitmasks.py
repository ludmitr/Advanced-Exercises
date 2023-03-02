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

def conforming_numbers(b_number: str) -> list:
    dict_number = {}
    for x in range(len(b_number)):
        if b_number[x] == "0": dict_number[x] = int(b_number[x])



    return b_number,dict_number




def main():
    a = conforming_numbers(bin(455)[2:])
    for x in a:
        print(x)
if __name__ == "__main__":
    main()