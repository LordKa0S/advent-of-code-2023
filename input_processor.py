from typing import List


def get_input() -> List[str]:
    lines: List[str] = []
    while True:
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
    return lines
