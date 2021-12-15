from aoc import aoc


def pilot_submarine(nav_log: list[str], aiming: bool = False) -> (int, int):
    x, y, aim_y = 0, 0, 0
    for line in nav_log:
        d, amount = line.split(' ')
        if d == 'up':
            y -= int(amount)
        elif d == 'down':
            y += int(amount)
        else:
            x += int(amount)
            if aiming:
                aim_y += y * int(amount)

    aoc.logger(f"Horizontal position: {x}; Depth: {aim_y if aiming else y}; "
               f"Resulting course: {(x * aim_y) if aiming else (x * y)}")
    return (x, y) if not aiming else (x, aim_y)


input = aoc.read_input('../input/in.txt')

x1, y1 = pilot_submarine(input)
x2, y2 = pilot_submarine(input, aiming=True)
