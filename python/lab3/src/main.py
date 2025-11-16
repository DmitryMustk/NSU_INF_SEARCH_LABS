from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Final

ENG_LOWER: Final[str] = "abcdefghijklmnopqrstuvwxyz"
ENG_UPPER: Final[str] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

RUS_LOWER: Final[str] = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
RUS_UPPER: Final[str] = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


@dataclass
class CaesarCipher:
    shift: int
    language: str

    def __post_init__(self) -> None:
        self.language = self.language.lower()

        if self.language not in ("eng", "rus"):
            raise ValueError("Language must be 'eng' or 'rus'.")

        if self.language == "eng":
            self.alphabet_lower = ENG_LOWER
            self.alphabet_upper = ENG_UPPER
        else:
            self.alphabet_lower = RUS_LOWER
            self.alphabet_upper = RUS_UPPER

        self.shift %= len(self.alphabet_lower)

    def encrypt_char(self, ch: str) -> str:
        if ch in self.alphabet_lower:
            index = self.alphabet_lower.index(ch)
            return self.alphabet_lower[(index + self.shift) % len(self.alphabet_lower)]

        if ch in self.alphabet_upper:
            index = self.alphabet_upper.index(ch)
            return self.alphabet_upper[(index + self.shift) % len(self.alphabet_upper)]

        return ch

    def encrypt_text(self, text: str) -> str:
        return "".join(self.encrypt_char(ch) for ch in text)

    def encrypt_file(self, input_path: str, output_path: str) -> None:
        try:
            with open(input_path, "r", encoding="utf-8") as f:
                text = f.read()
        except OSError as e:
            raise OSError(f"Could not read input file: {e}")

        encrypted = self.encrypt_text(text)

        try:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(encrypted)
        except OSError as e:
            raise OSError(f"Could not write output file: {e}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Caesar Cipher encryption for English or Russian text files."
    )
    parser.add_argument("-i", "--input", required=True, help="Path to input text file.")
    parser.add_argument("-o", "--output", required=True, help="Path to output file.")
    parser.add_argument("-s", "--shift", required=True, type=int, help="Shift value.")
    parser.add_argument(
        "-l",
        "--language",
        required=True,
        choices=["eng", "rus"],
        help="Language of text: eng or rus.",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    cipher = CaesarCipher(shift=args.shift, language=args.language)
    cipher.encrypt_file(args.input, args.output)

    print(f"Successfully encrypted → {args.output}")


if __name__ == "__main__":
    main()
