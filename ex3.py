from num2words import num2words
import re

def count_number_letter(num:int):
    """
    calculate amount of letters 1 to num

    Parameters:
    num(int): number to count from 1 to num in words

    Returns:
    int: number of letters from 1 to num
    """
    lettes_num =""
    for number in range(1,num+1):
        lettes_num += (num2words(number))
    
    lettes_num = re.sub(r'[^a-zA-Z]+', '', lettes_num)#remove all signs and spaces, return string of words

    return len(lettes_num) 

print(count_number_letter(1000))