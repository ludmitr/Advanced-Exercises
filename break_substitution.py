import string

book = "encrypted_book.txt"


def get_book_content(file_path):
    with open(file_path, encoding="utf8") as handle:
        return handle.read()


def encrypt_char(char, key):
    key = key % 26
    decimal_a, decimal_y, decimal_A, decimal_Y = 97, 122, 65, 90
    # Case when char is not letter - return char without encrypt
    if char not in string.ascii_letters:
      return char

    decimal_char = ord(char) + key
    # checking cases when encrypted char outside decimal range of letters => using modulo to put it in range
    # if it is in the range nothing of the if and elif will not apply
    if char.isupper():
      if decimal_char > decimal_Y:
        decimal_char = 64 + (ord(char) + key) % decimal_Y
    else:
      if decimal_char > decimal_y:
        decimal_char = 96 + (ord(char) + key) % decimal_y

    char = chr(decimal_char)
    return char


def encrypt_caesar(text, key):
    crypted_text = ""
    for char in text:
      crypted_text += encrypt_char(char, key)
    return crypted_text


def decrypt_caesar(ciphertext, key):
    key = -key
    uncrypred_text = ""
    for char in ciphertext:
      uncrypred_text += encrypt_char(char, key)
    return uncrypred_text

def frequency_analysis(text: str):
    """
    Creating dictionary where key is char and value is frequency of it occur in the text
    Returns:(dict) key is char(str) and val(int) its frequency
    """
    chars_frequency_dictionary = {}
    # removing upper case for analysis. assumptions of exercise  The mapping for the lower and the upper letters are the same
    text = text.lower()
    for char in text:
        #if char in letters(upper and lower casse)
        if char in string.ascii_letters:
            #if char not in dictionary - adding to dictionary and assigning value to 0
            if char not in chars_frequency_dictionary:
                chars_frequency_dictionary[char] = 0
            chars_frequency_dictionary[char] += 1
    return chars_frequency_dictionary


def main():
    encrypted_book = get_book_content(book)
    print(encrypted_book)


if __name__ == "__main__":
    main()
