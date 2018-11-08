with open("liczby1.txt", "r") as input1:
    data1 = input1.read()
    data1 = [int(x) for x in data1.split()]

with open("liczby2.txt", "r") as input2:
    data2 = input2.read()
    data2 = [int(x) for x in data2.split()]

# 1
smallest = float("inf")
highest = -float("inf")

for oct_number in data1:
    # ternary ftw
    smallest = oct_number if oct_number < smallest else smallest
    highest = oct_number if oct_number > highest else highest
print("1:", smallest, highest)

# 2


def find_sequence(data, index, count=1):
    if index+1 < len(data):
        if data[index+1] > data[index]:
            count += 1
            count = find_sequence(data, index+1, count)
    return count


longest_sequence = (0, -float("inf"))
i = 0

while i < len(data2):
    temp = find_sequence(data2, i)
    longest_sequence = (data2[i], temp) if temp > longest_sequence[1] else longest_sequence
    i += temp
print("2:", longest_sequence)

# 3


def to_dec(number, system):
    # piszę własny konwerter, wiem, że jest funkcja która konwertuje w bibliotece standardowej
    # (działa tylko w systemach 2-10)
    number = str(number)[::-1]
    result = 0
    for i, digit in enumerate(number):
        temp_digit = int(digit)
        if temp_digit != 0:
            result += temp_digit * system ** i
    return result


    # w zadaniu jest powiedziane, że data1 i data2 mają tyle samo elementów (1000)
higher_count, equal_count = 0, 0
smaller_count = 0
for i in range(len(data1)):
    if to_dec(data1[i], 8) > data2[i]:
        higher_count += 1
    elif to_dec(data1[i], 8) == data2[i]:
        equal_count += 1
print("3:", equal_count, higher_count)

# 4


def from_dec(number, system):
    # też działa tylko na systemy 2-10
    result = 0
    power = 0
    times = 1
    while number > 0:
        while system ** (power+1) < number:
            power += 1
        while (times+1) * (system ** power) <= number:
            times += 1
        number -= times * (system ** power)
        result += times * (10 ** power)
        power -= 1
        times = 1
    return result


dec_count = 0
oct_count = 0

for number in data2:
    if '6' in str(number):
        dec_count += 1
    if '6' in str(from_dec(number, 8)):
        oct_count += 1
print('4:', dec_count, oct_count)
