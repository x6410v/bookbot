from stats import get_word_count, get_book_text, char_count, sort_dict
import sys


def main():
    filepath = None
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]

    text: str = get_book_text(file_path=filepath)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(text)} total words")
    print("--------- Character Count -------")
    dlist = sort_dict(char_count(text))
    for i in dlist:
        char = i["char"]
        count = i["count"]
        print(f"{char}: {count}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
