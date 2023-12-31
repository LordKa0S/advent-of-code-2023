from input_processor import get_input

lines = get_input()

total = 0


def get_start_digit(text: str, position: int):
    digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for k, v in digits.items():
        if text[position:].startswith(k) or text[position:].startswith(v):
            return v
    return None


for line in lines:
    first_found, last_found = None, None
    position = 0
    while position < len(line) and (first_found is None or last_found is None):
        if first_found is None and (val := get_start_digit(line, position)) is not None:
            first_found = val
        if (
            last_found is None
            and (val := get_start_digit(line, -(position + 1))) is not None
        ):
            last_found = val
        position += 1
    if first_found is not None and last_found is not None:
        total += int(first_found + last_found)

print(total)
