import string

ALPHABET = string.ascii_uppercase


def encrypt(text, key):
    key = key.upper()

    if len(key) != 26:
        raise ValueError("Key must have 26 letters")

    mapping = dict(zip(ALPHABET, key))

    result = ""
    for char in text:
        if char.isalpha():
            upper_char = char.upper()
            new_char = mapping[upper_char]
            result += new_char if char.isupper() else new_char.lower()
        else:
            result += char

    return result


def decrypt(text, key):
    key = key.upper()

    mapping = dict(zip(key, ALPHABET))

    result = ""
    for char in text:
        if char.isalpha():
            upper_char = char.upper()
            new_char = mapping[upper_char]
            result += new_char if char.isupper() else new_char.lower()
        else:
            result += char

    return result


def generate_key():
    import random
    alphabet = list(ALPHABET)
    random.shuffle(alphabet)
    return "".join(alphabet)