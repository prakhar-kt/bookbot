from typing import Dict


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    return len(text.split())

def count_chars(text):
    char_count_dict = {}
    text = text.lower()
    for char in text:
        if char in char_count_dict:
            continue
        char_count_dict[char] = text.count(char)

    return char_count_dict

def sort_on(dict):
    return dict["num"]

def sort_char_counts(char_counts: Dict[str, int]):
    list_of_char_counts = []
    for key, val in char_counts.items():
        if key.isalpha():
            dict_new = {}
            dict_new["char"] = key
            dict_new["num"] = val
            list_of_char_counts.append(dict_new)
    list_of_char_counts.sort(reverse=True, key=sort_on)
    return list_of_char_counts
    