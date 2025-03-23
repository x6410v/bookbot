def get_word_count(text: str) -> int:
    split_text: list = text.split()
    count: int = 0
    for i in split_text:
        count += 1
    return count


def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        return f.read()


def char_count(text: str) -> dict:
    characters = {}
    for char in text:
        char = char.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters


def sort_on(dict):
    return dict["count"]


def sort_dict(dictionary: dict) -> list:
    dict_list = []

    for key in dictionary:
        value = dictionary[key]
        if key.isalpha():
            new_dict = {'char': key, 'count': value}
            dict_list.append(new_dict)
        else:
            pass
    dict_list.sort(key=sort_on, reverse=True)
    return dict_list
