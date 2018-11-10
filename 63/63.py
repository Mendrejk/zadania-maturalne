from math import sqrt

with open("ciagi.txt", "r") as input_file:
    data = input_file.read()
data = data.split()

# 1
bicyclic_sequences = []

for sequence in data:
    half = len(sequence)/2
    if int(half) == half:
        half = int(half)
        if sequence[:half] == sequence[half:]:
            bicyclic_sequences.append(sequence)
print("1:", bicyclic_sequences)

# 2
count = 0

for sequence in data:
    sad = 0
    for i in range(len(sequence)-1):
        if sequence[i] == "1":
            if sequence[i+1] == "1":
                sad = 1
    if sad == 1:
        continue
    else:
        count += 1
print("2:", count)

# 3:
count = 0
smallest = float("inf")
largest = -float('inf')

for sequence in data:
    number = int(sequence, 2)
    temp = number
    dividers = []
    sad = False

    for i in range(2, int(number/2)):
        if len(dividers) > 2 or (dividers is False and i > sqrt(dividers)):
            sad = True
            break
        if temp % i == 0:
            temp /= i
            dividers.append(i)
    if sad:
        continue
    if len(dividers) == 2:
        count += 1
        smallest = number if number < smallest else smallest
        largest = number if number > largest else largest
print(count, smallest, largest)
