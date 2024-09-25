def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = get_character_count(text)
    print(f"{num_words} words found in the document")
    print(f"{char_counts}")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    text = text.lower()
    letters = {}
    for i in text:
        letters[i] = letters.get(i, 0) + 1
    return letters

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()