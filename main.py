import sys

from stats import read_book, get_word_count, sorting_characters


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text = read_book(book_path)
    word_count = get_word_count(text)
    sorted_char = sorting_characters(text)

    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...")  
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print("\n".join(sorted_char))
    print("============= END ===============")
if __name__ == "__main__":
    main()
