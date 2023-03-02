import string

book_file_name = "encrypted_book.txt"


def get_book_content(file_path):
    with open(file_path, encoding="utf8") as handle:
        return handle.read()


def sort_dictionary_by_value(dictionary: dict):
    """
    Creates dictionary with descending order by its value

    Returns: dictionary with descending order by its value
    """
    # creating copy of dictionary for local logic
    temp_dictionary = dictionary.copy()
    descending_dictionary = {}
    for x in range(len(dictionary)):
        highest_value, highest_key = 0, ""
        for key, val in temp_dictionary.items():
            if val > highest_value:
                highest_value = val
                highest_key = key

        descending_dictionary[highest_key] = highest_value
        del temp_dictionary[highest_key]
    return descending_dictionary


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

def decrypt_text(text,dictionary):
    new_dictionary = {
        "i":"e", "k":"t", "x":"a", "u":"o", "t":"i",
        "w":"n", "a":"s", "r":"r", "f":"h", "c":"d",
        "n":"l", "v":"m", "h":"c", "j":"y", "z":"g",
        "d":"f", "o":"u", "m":"w", "q":"p",  "e":"k",
        "l":"v", "s":"j", "b":"b",  "p":"q", "g":"x",
        "y":"z"
    }


    new_text = ""
    for char in text:
        if char.lower() in new_dictionary:
            if char.islower():
                new_text += new_dictionary[char]
            else:
                new_text += new_dictionary[char].upper()


    return new_text
def main():
    encrypted_book = get_book_content(book_file_name)
    temp_dictionary = frequency_analysis(encrypted_book)
    temp_dictionary = sort_dictionary_by_value(temp_dictionary)
    temp_dictionary = decrypt_text(encrypted_book,temp_dictionary)

    print(temp_dictionary)
    # for x, y in temp_dictionary.items():
    #     print(f"{x}:  {y}")


if __name__ == "__main__":
    main()
