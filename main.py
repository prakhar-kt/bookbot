import sys
from stats import count_words, get_book_text, count_chars, sort_char_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    frankenstein_filepath = sys.argv[1]
    content = get_book_text(frankenstein_filepath)
    num_words = count_words(content)
    char_counts = count_chars(content)
    list_of_char_counts = sort_char_counts(char_counts)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in list_of_char_counts:
        print(f'{item["char"]}: {item["num"]}')
    
    


main()