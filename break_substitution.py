import string
import chardet

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


def main():
    encrypted_book = get_book_content(book)
    print(encrypted_book)


if __name__ == "__main__":
    main()
