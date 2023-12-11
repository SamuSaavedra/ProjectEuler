# Problem 3: Largest Prime Factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143

import numpy as np

def factor_list(number):
    """Creates a list of all factors of a number

    Args:
        number (int): Number from which the factors are calculated

    Returns:
        list: List of all factors of the number
    """
    factors = []
    s_root = int(np.sqrt(number))
    for i in range(s_root):
        calculation = number % (i + 1)
        if calculation == 0:
            factors.append(i + 1)
    for factor in factors[:]:  # Calculates the second half of the multiplies
        factors.append(int(number / factor))
    if factors.count(factors[-1]) == 2:  # If it's a perfect square removes one of the copies of the square root
        factors.remove(factors[-1])
    factors.sort()
    return factors

def is_prime(number):
    """Checks if a number is prime or not

    Args:
        number (int): Number that needs to be checked if it's prime

    Returns:
        bool: Returns True if it's prime and False if it's not
    """
    s_root = int(np.sqrt(number))
    for i in range(s_root):
        if number % (i + 1) == 0 and (i + 1) != 1:
            return False
    else:
        return True


NUMBER = 600851475143

factors = factor_list(NUMBER)
del factors[0]
del factors[-1]
factors.sort(reverse=True)
for factor in factors:
    if is_prime(factor):
        print(factor)
        break