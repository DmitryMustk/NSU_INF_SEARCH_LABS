from __future__ import annotations

import argparse
from typing import Final


VALID_OPEN: Final[str] = "("
VALID_CLOSE: Final[str] = ")"


def is_correct_bracket_sequence(seq: str) -> bool:
    balance = 0

    for ch in seq:
        if ch == VALID_OPEN:
            balance += 1
        elif ch == VALID_CLOSE:
            balance -= 1
            if balance < 0:
                return False
        else:
            return False

    return balance == 0


def read_sequence_from_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        line = f.readline()
    return line.strip()


def read_sequence_from_stdin() -> str:
    return input("Enter bracket sequence: ").strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Check if a bracket sequence (consisting of '(' and ')') is correct."
        )
    )
    parser.add_argument(
        "-f",
        "--file",
        help="Path to a file containing the bracket sequence (first line is used).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.file:
        try:
            seq = read_sequence_from_file(args.file)
        except OSError as e:
            print(f"Error: could not read file: {e}")
            return
    else:
        seq = read_sequence_from_stdin()

    if not seq:
        print("Error: empty sequence is not valid.")
        return

    if is_correct_bracket_sequence(seq):
        print(f"Sequence '{seq}' is CORRECT.")
    else:
        print(f"Sequence '{seq}' is INCORRECT.")


if __name__ == "__main__":
    main()
