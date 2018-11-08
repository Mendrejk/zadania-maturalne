from math import pow
from statistics import mode


with open("ciagi.txt", "r") as input_file:
    data = input_file.read()

data = data.splitlines()

sequences = []
for i in range(0, len(data), 2):
    sequences.append([data[i], data[i+1]])

# 1
highest_difference = 0
count_of_arithmetic = 0

for i in sequences:
    is_arithmetic = True
    sequence = i[1]

    # konwertuje stringa w listę intów
    sequence = [int(x) for x in sequence.split()]

    difference = sequence[1] - sequence[0]

    for j, number in enumerate(sequence):
        # jeśli poniższe się nie równa, to ciąg nie jest arytmetyczny
        if number != sequence[0] + difference*j:
            is_arithmetic = False
            break
    if not is_arithmetic:
        continue
    count_of_arithmetic += 1
    if difference > highest_difference:
        highest_difference = difference
print(count_of_arithmetic, highest_difference)

# 2
highest_cubes = []
for i in sequences:
    highest_cube = 0
    sequence = i[1]

    sequence = [int(x) for x in sequence.split()]

    for number in sequence:
        for j in range(number):
            if j**3 > number:
                break
            elif j**3 == number:
                if number > highest_cube:
                    highest_cube = number
    if highest_cube != 0:
        highest_cubes.append(highest_cube)
print(highest_cubes)

# 3
with open("bledne.txt", "r") as bledny_input_file:
    bledne_data = bledny_input_file.read()

bledne_data = bledne_data.splitlines()

bledne_sequences = []
for i in range(0, len(bledne_data), 2):
    bledne_sequences.append([bledne_data[i], bledne_data[i+1]])

bledne_wyrazy = []

for i in bledne_sequences:
    bledne_roznice = []
    bledne_sequence = i[1]
    bledne_sequence = [int(x) for x in bledne_sequence.split()]
    most_common_difference = 0

    for j in range(len(bledne_sequence)-1):
        bledne_roznice.append(bledne_sequence[j+1] - bledne_sequence[j])
    most_common_difference = mode(bledne_roznice)

    for j, roznica in enumerate(bledne_roznice):
        if roznica != most_common_difference:
            if j == 0:
                bledne_wyrazy.append(bledne_sequence[0])
                break
            else:
                # tu teoretycznie mozliwe jest wyjscie out of bonds, ale tak naprade nie jest mozliwe, bo jest jest bledny element to poprzedni tez bedzie bledny
                bledne_wyrazy.append(bledne_sequence[j+1])
                break
print(bledne_wyrazy)
