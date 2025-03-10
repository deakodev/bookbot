import sys
from stats import get_word_count
from stats import get_char_count
from stats import sort_char_dict

def get_book_text(path_to_file):
    file_contents = ""

    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    print("============ BOOKBOT ============")

    file_path = sys.argv[1]

    print(f"Analyzing book found at {file_path}...")

    text = get_book_text(file_path)
    num_words = get_word_count(text)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    num_chars = get_char_count(text)
    
    print("--------- Character Count -------")
    for dict in sort_char_dict(num_chars):
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["count"]}")

    print("============= END ===============")

main()