def count_words(text):
    if not isinstance(text, str):
        raise ValueError("Input to count_words must be a string.")
    words = text.split()
    return len(words)

def count_characters(text):
    """
    Counts the number of times each character appears in the text.
    Converts all characters to lowercase to avoid duplicates.

    Parameters:
        text (str): The full text of the book.

    Returns:
        dict: A dictionary with characters as keys and their counts as values.
    """
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_character_counts(char_dict):
    """
    Converts a character count dictionary into a sorted list of dictionaries.
    Each dictionary has keys 'char' and 'num'.
    Sorted from greatest to least by 'num'.

    Parameters:
        char_dict (dict[str, int]): Dictionary of character counts.

    Returns:
        list[dict[str, int]]: Sorted list of character count dictionaries.
    """
    # Convert to list of dictionaries
    char_list = [{"char": k, "num": v} for k, v in char_dict.items()]

    # Helper function for sorting
    def get_count(item):
        return item["num"]

    # Sort the list in descending order
    char_list.sort(key=get_count, reverse=True)

    return char_list
