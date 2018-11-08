from math import ceil

with open("liczby.txt", 'r') as input_file:
    data = input_file.read()

data = data.splitlines()
for i in range(len(data)):
    data[i] = int(data[i])

# 1
previous_small, small = 0, 0
counter = 0

for number in data:
    if number < 1000:
        counter += 1
        previous_small = small
        small = number
print("1: Counter: {}, 2nd last: {}, last: {}".format(counter, previous_small, small))

# 2
numbers_and_eighteen_dzielniks = []
for number in data:
    dzielnikis = [1]
    for i in range(2, ceil(number/2)+1):
        if len(dzielnikis) > 17:
            break
        elif number % i == 0:
            dzielnikis.append(i)
    if len(dzielnikis) == 17:
        dzielnikis.append(number)
        numbers_and_eighteen_dzielniks.append([number, dzielnikis])
print("2:", numbers_and_eighteen_dzielniks)

# 3
numbers_and_dzielniks = []
for number in data:
    if number % 2 == 1:
        dzielnikis = [1, number]
        for i in range(2, ceil(number/2)+1):
            if number % i == 0:
                dzielnikis.append(i)
        numbers_and_dzielniks.append([number, dzielnikis])

# to jest brzydkie, ale działa (i to on dziwo szybko), a na maturze nie będę znał z głowy żadnych fancy argorytmów z nwd czy nww
# to co się tu dzieje, to sprawdzam po kolei czy każdy dzielnik liczby nie występuje wśród dzielników innych liczb
highest_non_dzielnik = 0
for number_and_dzielniks in numbers_and_dzielniks:
    sad = False
    for dzielnik in number_and_dzielniks[1]:
        if dzielnik == 1:
            continue
        if sad:
            break
        for other_number_and_dzielniks in numbers_and_dzielniks:
            if other_number_and_dzielniks[0] == number_and_dzielniks[0]:
                continue
            elif dzielnik in other_number_and_dzielniks[1]:
                sad = True
                break
    if sad:
        continue
    elif number_and_dzielniks[0] > highest_non_dzielnik:
        highest_non_dzielnik = number_and_dzielniks[0]
print("3:", highest_non_dzielnik)
