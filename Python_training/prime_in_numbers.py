# Given a positive number n > 1 find the prime factor decomposition of n. 
# The result will be a string with the following form :

#  "(p1**n1)(p2**n2)...(pk**nk)"
# with the p(i) in increasing order and n(i) empty if n(i) is 1.

# Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
import math

def prime_factors(n):
    pass
    
def is_prime(primes,n):
    max_value = math.ceil(math.sqrt(n))
    count = 0
    rem = n%primes[count]
    while primes[count] < max_value and rem != 0:
        count += 1
        rem = n%primes[count]
    if rem == 0:
        return False
    else:
        return True
        
def next_prime(primes):
    found_prime = False
    guess_prime = primes[-1]
    while not(found_prime):
        guess_prime += 1
        if is_prime(primes, guess_prime):
            found_prime = True
        
    primes.append(guess_prime)
    return primes

def order_prime(prime, n):
    order = 0
    rest = n%prime
    quotient = n//prime
    while rest == 0:
        rest = quotient%prime
        quotient = quotient//prime
        order += 1
    return order
def main():
    # print(order_prime())
main()