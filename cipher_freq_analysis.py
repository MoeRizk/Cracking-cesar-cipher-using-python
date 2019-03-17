from collections import Counter
from collections import OrderedDict
import re


def get_the_value(cipher):
    list = []
    dict = {}
    pure_list = []
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cleaned_cipher = clean_text_from_special_char(cipher)
    cleaned_cipher = clean_text_from_numbers(cleaned_cipher)
    cleaned_cipher = cleaned_cipher.replace(" ", "")
    cleaned_cipher = cleaned_cipher.replace(".", "")
    cleaned_cipher = cleaned_cipher.replace("\ufeff", "")
    cipher_letter_count = len(cleaned_cipher)
    the_char_count_in_cleaned_cipher = Counter(cleaned_cipher)

    for letter in the_char_count_in_cleaned_cipher:
        dict[letter] = (the_char_count_in_cleaned_cipher[letter] / cipher_letter_count)
        list.append(the_char_count_in_cleaned_cipher[letter] / cipher_letter_count)

    sorted_dict = OrderedDict(sorted(dict.items()))
    dict_with_complete_letters = {}

    for aplha_letter in LETTERS:
        if aplha_letter in sorted_dict:
            dict_with_complete_letters[aplha_letter] = sorted_dict[aplha_letter]
        else:
            dict_with_complete_letters[aplha_letter] = float(0.0)

    for k, v in sorted(dict_with_complete_letters.items()):
        pure_list.append(v)

    return pure_list

def clean_text_from_special_char(the_cipher):
    cipher_without_special_char = ''
    for k in the_cipher.split("\n"):
        cipher_without_special_char = cipher_without_special_char + (re.sub(r"[^a-zA-Z0-9]+", ' ', k))

    return cipher_without_special_char

def clean_text_from_numbers(the_cipher):
    cipher_without_numbers = ''
    for k in the_cipher.split("\n"):
        cipher_without_numbers = cipher_without_numbers + (re.sub('[0-9]', '', k))

    return cipher_without_numbers
