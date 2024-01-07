from input_processor import get_input

lines = get_input()

total = 0

for game_line in lines:
    game_meta, game_details = map(str.strip, game_line.split(":"))
    handfuls = tuple(map(str.strip, game_details.split(";")))
    max_color = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for handful in handfuls:
        count_colors = map(str.strip, handful.split(","))
        for count_color in count_colors:
            count, color = map(str.strip, count_color.split())
            max_color[color] = max(max_color[color], int(count))
    product = 1
    for count in max_color.values():
        product *= count
    total += product

print(total)
