# Largest palindrome product
# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


number = 0

for x in range(999,100,-1):
    for y in range(x,100,-1):
        product = x*y
        check = str(x*y)

        if check == check[::-1]:
            if product > number:
                number = product

print(number)
