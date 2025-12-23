import sys

from stats import char_mentions, get_word_count, sort_chars

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]


def get_book_text(fpath):
    with open(fpath) as f:
        file_contents = f.read()
        return file_contents


def main():
    book_text = get_book_text(book_path)
    num_words = get_word_count(book_text)
    char_count = char_mentions(book_text)
    sorted_char_dict = sort_chars(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in sorted_char_dict.items():
        if char[0].isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")


main()
