def get_word_count(book_text):
    words = book_text.split()
    return len(words)


def char_mentions(book_text):
    char_count = {}
    book_text = book_text.lower()
    for char in book_text:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count


def sort_chars(char_dir):
    new_char_dir = dict(
        sorted(char_dir.items(), key=lambda item: item[1], reverse=True)
    )
    return new_char_dir
