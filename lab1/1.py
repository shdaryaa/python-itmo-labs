GREEN = '\u001b[42m'
RED = '\u001b[41m'
END = '\u001b[0m'
radius = 4


def is_inside_circle(x, y, center_x, center_y, radius):
    return (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2

center_x = 6
center_y = 15

for x in range(13):
    for y in range(41):
        if is_inside_circle(x, y, center_x, center_y, radius):
            print(f"{RED} {END}", end='')
        else:
            print(f"{GREEN} {END}", end='')
    print()
