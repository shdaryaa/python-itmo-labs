def read_data_from_file(filename):
    with open(filename) as file:
        result = list()
        for num_str in file:
            result.append(float(num_str))
        return result


data_from_file = read_data_from_file('sequence.txt')

sum_first = 0
for i in range(125):
    sum_first += abs(data_from_file[i])

sum_last = 0
for i in range(len(data_from_file) - 125, len(data_from_file)):
    sum_last += abs(data_from_file[i])


print(f'Sum first: {sum_first}')
print(f'Sum last: {sum_last}')