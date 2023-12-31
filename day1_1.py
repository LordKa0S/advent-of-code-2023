from input_processor import get_input

lines = get_input()

total = 0

for line in lines:
    first_found, last_found = None, None
    position = 0
    while position < len(line) and (first_found is None or last_found is None):
        if first_found is None and line[position].isdigit():
            first_found = line[position]
        if last_found is None and line[-(position + 1)].isdigit():
            last_found = line[-(position + 1)]
        position += 1
    if first_found is not None and last_found is not None:
        total += int(first_found + last_found)

print(total)
