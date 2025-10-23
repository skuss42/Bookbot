from stats import count_words, count_characters, sort_character_counts
import sys

def get_book_text(filepath):
    """
    Reads the contents of a file and returns it as a string.

    Parameters:
        filepath (str): The path to the file.

    Returns:
        str: The full text content of the file.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error: {e}"

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print(f"Analyzing book found at {book_path}...")

    text = get_book_text(book_path)

    if text.startswith("Error:"):
        print(text)
        print("============= END ===============")
        return

    try:
        word_count = count_words(text)
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
    except Exception as e:
        print(f"Error counting words: {e}")
        print("============= END ===============")
        return

 # Check for file read errors
    if text.startswith("Error:"):
        print(text)
        print("============= END ===============")
        return
    
    print(f"DEBUG: type(text) = {type(text)}")
    print(f"DEBUG: preview = {text[:100]}")
    # Count and sort characters
    char_counts = count_characters(text)
    sorted_chars = sort_character_counts(char_counts)

    # Print character counts
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

#  This was missing
if __name__ == "__main__":
    main()
