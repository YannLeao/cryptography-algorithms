import os
from pathlib import Path

from algorithms.caesar import encrypt as caesar_encrypt, decrypt as caesar_decrypt, generate_key as caesar_generate
from algorithms.hill import encrypt as hill_encrypt, decrypt as hill_decrypt, generate_key as hill_generate
from algorithms.mono_alphabetic import (encrypt as mono_alphabetic_encrypt, decrypt as mono_alphabetic_decrypt,
                                        generate_key as mono_alphabetic_generate)
from algorithms.playfair import (encrypt as playfair_encrypt, decrypt as playfair_decrypt,
                                 generate_key as playfair_generate)

BASE_DIR = Path(__file__).resolve().parent

ALGORITHMS = {
    "Caesar": {
        "encrypt": caesar_encrypt,
        "decrypt": caesar_decrypt,
        "generate_key": caesar_generate
    },
    "Mono-alphabetic": {
        "encrypt": mono_alphabetic_encrypt,
        "decrypt": mono_alphabetic_decrypt,
        "generate_key": mono_alphabetic_generate
    },
    "Playfair": {
        "encrypt": playfair_encrypt,
        "decrypt": playfair_decrypt,
        "generate_key": playfair_generate
    },
    "Hill": {
        "encrypt": hill_encrypt,
        "decrypt": hill_decrypt,
        "generate_key": hill_generate
    },
}

# UI/UX
THEME_PATH = BASE_DIR / "ui" / "theme" / "theme.json"
FONT_PATH = BASE_DIR / "ui" / "font" / "JetBrainsMono-Regular.ttf"
BACKGROUND_COLOR = "#0E130E"
BARS_COLOR = "#00E68A"
TEXT_COLOR = "#9EFFC8"


def load_custom_font():
    if os.name == 'nt':
        try:
            from ctypes import windll
            path_str = str(FONT_PATH.absolute())
            windll.gdi32.AddFontResourceExW(path_str, 0x10, 0)

        except Exception as e:
            print(f"Erro ao carregar fonte: {e}")
