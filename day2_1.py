from input_processor import get_input

lines = get_input()

total = 0

for game_line in lines:
    valid = True
    game_meta, game_details = map(str.strip, game_line.split(":"))
    handfuls = tuple(map(str.strip, game_details.split(";")))
    for handful in handfuls:
        if not valid:
            break
        count_colors = map(str.strip, handful.split(","))
        for count_color in count_colors:
            if not valid:
                break
            count, color = map(str.strip, count_color.split())
            if (
                (color == "red" and int(count) > 12)
                or (color == "green" and int(count) > 13)
                or (color == "blue" and int(count) > 14)
            ):
                valid = False
                break
    if valid:
        _, game_id = map(str.strip, game_meta.split())
        total += int(game_id)

print(total)
