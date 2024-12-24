def get_book_content(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        f.close()
        return file_contents
    
def get_word_amt(book_content):
    return len(book_content.split())


        

def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_content(book_path)
    print(get_word_amt(text))
        
if __name__ == "__main__":
    main()