
# returns True if parameter n is a prime number, False if composite and "Neither prime, nor composite" if neither
def isPrime(n):
    if n < 2: return "notprime"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

sum = 0
for i in range(2, 2000000):
    if isPrime(i):
        sum += i

print (sum)
