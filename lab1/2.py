WHITE = '\u001b[47m'
END = '\u001b[0m'

times = 5

for i in range(5):
    line = ''
    for j in range(times):
        if i != 4 and j != 0:
            if i == 3:
                line += f'{' ' * 8}'
            else:
                line += f'{' ' * 4}'
        if i == 0:
            line += f'{WHITE}{' ' * 10}{END}'
        elif i == 1:
            line += f'{WHITE}{' ' * 2}{END}{' ' * 6}{WHITE}{' ' * 2}{END}'
        elif i == 2:
            line += f'{WHITE}{' ' * 2}{END}{' ' * 2}{WHITE}{' ' * 6}{END}'
        elif i == 3:
            line += f'{WHITE}{' ' * 2}{END}{' ' * 2}{WHITE}{' ' * 2}{END}'
        else:
            line += f'{WHITE}{' ' * 2}{END}{' ' * 2}{WHITE}{' ' * 10}{END}'
    print(line)
