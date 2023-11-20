# Problem 1: Multiples of 3 or 5.
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

TOP_NUMBER = 1000
divisors = 3, 5
multiples = []  # Each number that is multiple of divisors

for divisor in divisors:
    max_divisor = int(TOP_NUMBER / divisor)  # [333, 200]
    for i in range(max_divisor):
        multiples.append(divisor * (i + 1))

multiples = list(set(multiples))  # Deletion of duplicated values

if TOP_NUMBER in multiples:  # ... sum of all the multiplies BELOW ...
    multiples.remove(TOP_NUMBER)

print(sum(multiples))