import random
import string

from wordfreq import top_n_list


def encrypt(text, key):
    matrix = generate_matrix(key)
    text = prepare_text(text)

    result = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]

        row_1, column_1 = find_position(matrix, a)
        row_2, column_2 = find_position(matrix, b)

        if row_1 == row_2:
            result += matrix[row_1][(column_1 + 1) % 5]
            result += matrix[row_2][(column_2 + 1) % 5]

        elif column_1 == column_2:
            result += matrix[(row_1 + 1) % 5][column_1]
            result += matrix[(row_2 + 1) % 5][column_2]

        else:
            result += matrix[row_1][column_2]
            result += matrix[row_2][column_1]

    return result


def decrypt(text, key):
    matrix = generate_matrix(key)
    text = prepare_text(text)

    result = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]

        row_1, column_1 = find_position(matrix, a)
        row_2, column_2 = find_position(matrix, b)

        if row_1 == row_2:
            result += matrix[row_1][(column_1 - 1) % 5]
            result += matrix[row_2][(column_2 - 1) % 5]

        elif column_1 == column_2:
            result += matrix[(row_1 - 1) % 5][column_1]
            result += matrix[(row_2 - 1) % 5][column_2]

        else:
            result += matrix[row_1][column_2]
            result += matrix[row_2][column_1]

    return result


def generate_key():
    words = top_n_list("en", 5000)
    return random.choice(words)


def generate_matrix(key):
    key = key.upper().replace("J", "I")
    seen = set()
    matrix = []

    for char in key + string.ascii_uppercase:
        if char not in seen and char.isalpha():
            if char == "J":
                continue
            seen.add(char)
            matrix.append(char)
    return [matrix[i:i + 5] for i in range(0, 25, 5)]


def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = "".join([char for char in text if char.isalpha()])

    result = ""

    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else "X"

        if a == b:
            result += a + "X"
            i += 1
        else:
            result += a + b
            i += 2
    if len(result) % 2 != 0:
        result += "X"

    return result


def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if char == matrix[i][j]:
                return i, j
