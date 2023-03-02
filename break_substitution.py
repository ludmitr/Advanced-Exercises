import string

book = "encrypted_book.txt"


def get_book_content(file_path):
    with open(file_path, encoding="utf8") as handle:
        return handle.read()


def frequency_analysis(text: str):
    """
    Creating dictionary where key is char and value is frequency of it occur in the text
    Returns:(dict) key is char(str) and val(int) its frequency
    """
    chars_frequency_dictionary = {}
    # removing upper case for analysis. assumptions of exercise
    # The mapping for the lower and the upper letters are the same
    text = text.lower()

    for char in text:
        # if char in letters
        if char in string.ascii_letters:
            # if char not in dictionary - adding to dictionary and assigning value to 0
            if char not in chars_frequency_dictionary:
                chars_frequency_dictionary[char] = 0
            chars_frequency_dictionary[char] += 1
    return chars_frequency_dictionary


def main():
    encrypted_book = get_book_content(book)
    temp_dictionary = frequency_analysis(encrypted_book)
    for x, y in temp_dictionary.items():
        print(f"{x}:  {y}")


if __name__ == "__main__":
    main()
