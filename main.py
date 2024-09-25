def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = get_character_count(text)
    print(f"{num_words} words found in the document")
    print(f"{char_counts}")

# Function to sort the char_count dictionary.
def sort_on(dict):
    return dict["num"]

# Function to count the number of words within the book / text
def get_num_words(text):
    words = text.split()
    return len(words)

# Function to count the occurrence of each letter within the book / text
def get_character_count(text):
    text = text.lower()
    letters = {}
    for i in text:
        letters[i] = letters.get(i, 0) + 1
    return letters

# Function to pull the book / text into the program
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()