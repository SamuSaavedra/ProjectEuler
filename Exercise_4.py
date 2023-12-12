# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindromic(number):
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False

MAX_3_DIGIT = 999
MIN_3_DIGIT = 100
largest_palindrome = int()

for i in range(MAX_3_DIGIT - MIN_3_DIGIT):
    number_1 = MAX_3_DIGIT - i
    for j in range(MAX_3_DIGIT - MIN_3_DIGIT):
        number_2 = MAX_3_DIGIT - j
        product = number_1 * number_2
        if is_palindromic(product):
            if product > largest_palindrome:
                largest_palindrome = product

print(largest_palindrome)