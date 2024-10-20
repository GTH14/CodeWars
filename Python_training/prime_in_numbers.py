# Given a positive number n > 1 find the prime factor decomposition of n. 
# The result will be a string with the following form :

#  "(p1**n1)(p2**n2)...(pk**nk)"
# with the p(i) in increasing order and n(i) empty if n(i) is 1.

# Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
import math

def prime_factors(n):
    factors = []
    orders = []
    factor_msg = ""
    primes = [2]
    count_factors = 0
    count_primes = 0
    quotient = n
    while quotient != 1:
        remainder = quotient%primes[count_primes]
        if remainder == 0:
            factors.append(primes[count_primes])
            orders.append(order_prime(primes[count_primes], quotient))
            quotient = quotient//(primes[count_primes]**orders[count_factors])
            count_factors += 1
        count_primes += 1
        primes = next_prime(primes)
    
    for index in range(len(factors)):
        if orders[index] != 1:
            factor_msg += "(" + str(factors[index]) + "**" + str(orders[index]) + ")"
        else:
            factor_msg += "(" + str(factors[index]) + ")"
    return factor_msg
    
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
    # pass
    n = 97
    print(prime_factors(n))
main()