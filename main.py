from stats import *
import sys


def get_book_text(path):
    with open(path) as f:
        book_content = f.read()
        return book_content
    
    
def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


def main():
    if len(sys.argv)<2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book = get_book_text(book_path)
    num_words = count_words(book)
    alphabet = count_characters(book)
    chars_sorted_list=sort_list_char(alphabet)
    print_report(book_path, num_words, chars_sorted_list) 

main()