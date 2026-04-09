import numpy as np
import string

ALPHABET = string.ascii_uppercase
MOD = 26


def encrypt(text, key):
    key_matrix = np.array(key)
    size = key_matrix.shape[0]

    text = prepare_text(text, size)
    numbers = text_to_numbers(text)

    result = []

    for i in range(0, len(numbers), size):
        block = np.array(numbers[i:i + size])
        encrypted = key_matrix.dot(block) % MOD
        result.extend(encrypted)

    return numbers_to_text(result)


def decrypt(text, key):
    key_matrix = np.array(key)
    size = key_matrix.shape[0]

    try:
        inv_matrix = matrix_mod_inv(key_matrix, MOD)
    except ValueError:
        raise ValueError("Matrix is not invertible modulo 26")

    numbers = text_to_numbers(text)

    result = []

    for i in range(0, len(numbers), size):
        block = np.array(numbers[i:i + size])
        decrypted = inv_matrix.dot(block) % MOD
        result.extend(decrypted)

    return numbers_to_text(result)


def generate_key(size=2):
    while True:
        matrix = np.random.randint(0, 26, (size, size))
        if is_invertible(matrix):
            return matrix.tolist()


def text_to_numbers(text):
    return [ALPHABET.index(c) for c in text]


def numbers_to_text(numbers):
    return ''.join(ALPHABET[n % MOD] for n in numbers)


def prepare_text(text, size):
    text = text.upper().replace(" ", "")
    text = ''.join(c for c in text if c in ALPHABET)

    # padding com X
    while len(text) % size != 0:
        text += "X"

    return text


def matrix_mod_inv(matrix, mod):
    det = int(round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, mod)

    matrix_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int)
    return matrix_inv % mod


def is_invertible(matrix):
    det = int(round(np.linalg.det(matrix)))
    return np.gcd(det, MOD) == 1
