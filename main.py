def main():
    path_to_book = "./books/frankenstein.txt"
    book_content = read_book_text(path_to_book)
    words_in_book = count_words(book_content)
    repeating_chars = count_repeating_chars(book_content)
    sorted_chars = dict_to_sorted_list(repeating_chars)

    print(f"--- Begin report of {path_to_book} ---")
    print(f"{words_in_book} words found in the document")
    print()

    for item in sorted_chars:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def on_sort(dict):
    return dict["num"]


def dict_to_sorted_list(chars_num):
    sorted_list = []
    for char in chars_num:
        sorted_list.append({"char": char, "num": chars_num[char]})
    sorted_list.sort(reverse=True, key=on_sort)
    return sorted_list


def count_repeating_chars(text):
    chars = {}
    text_in_book = text.lower()
    text_in_book.isalpha()
    for char in text_in_book:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


def read_book_text(path):
    with open(path) as file:
        return file.read()


def count_words(text):
    words = text.split()
    return len(words)


main()
