from math import gcd

def read_file(file):
    with open(file, 'r') as input:
        data = input.read()
    data = data.split('\n')
    return data

data = read_file('dane_ulamki.txt')
for i in range(len(data)):
    data[i] = data[i].split()
    data[i][0], data[i][1] = int(data[i][0]), int(data[i][1])

#1
minimal_value = float('inf')
minimal_pairs = []

for pair in data:
    quotient = pair[0]/pair[1] 
    if quotient <= minimal_value:
        if quotient < minimal_value:
            minimal_pairs = [[pair[0],pair[1]]]
        else:
            minimal_pairs.append([pair[0],pair[1]])
        minimal_value = quotient

minimal_dividend = float('inf')
minimalest_pair = []
for pair in minimal_pairs:
    if pair[0] < minimal_dividend:
        minimal_dividend = pair[0]
        minimalest_pair = pair
print(minimalest_pair)

#2
count_of_half_prime_pairs = 0
for pair in data:
    if gcd(pair[0], pair[1]) == 1:
        count_of_half_prime_pairs += 1
print(count_of_half_prime_pairs)

#3
sum_divident = 0
new_pairs = []
temp_pair = [1, 1]
div, gdiv = 1, 1
for pair in data:
    temp_pair = pair
    while gcd(temp_pair[0], temp_pair[1]) > 1:
        div = gcd(temp_pair[0], temp_pair[1])
        temp_pair[0] //= div
        temp_pair[1] //= div
    sum_divident += temp_pair[0]
print(sum_divident)

#4
max_divisor = (2**2)*(3**2)*(5**2)*(7**2)*13 #573300
max_pairs = []
temp_pair = [1, 1]
max_div = 1
max_sum_pair = [0, max_divisor]
for pair in data:
    temp_pair = pair
    max_div = max_divisor/pair[1]
    temp_pair[0] *= max_div
    temp_pair[1] *= max_div
    max_sum_pair[0] += temp_pair[0]
print(max_sum_pair[0], max_sum_pair[0]/max_sum_pair[1])

