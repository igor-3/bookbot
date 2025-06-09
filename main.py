import sys
from stats import count_words, count_characters, sort_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    path = sys.argv[1]
    text = get_book_text(f"./{path}")
    word_count = count_words(text)
    character_count = count_characters(text)
    sorted_chars = sort_dictionary(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for d in sorted_chars:
        if d["char"].isalpha():
            print(d["char"] + ": " + str(d["num"]))
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
main()