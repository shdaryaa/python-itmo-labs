def draw_function():

    x_range = range(1, 10)
    y_range = range(1, 25)

    function_values = {x: 2 * x + 3 for x in x_range}

    for y in reversed(y_range):
        line = f"{y}\t"
        for x in x_range:
            if function_values[x] == y:
                line += "**"
            else:
                line += "--"
        print(line)
    x_labels = "\t" + ' '.join(str(x) for x in x_range)
    print(x_labels)

draw_function()
