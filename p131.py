from math import sqrt, pow
from __builtin__ import True

#------------------------------------------------
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# encontrando primos
LIMIT = 1000000

is_prime = [True]*LIMIT
is_prime[0] = False
is_prime[1] = False


for i in xrange(2,int(sqrt(LIMIT))):
    if is_prime[i]:
        j = i
        x = i*j
        while x < LIMIT:
            is_prime[x] = False
            j += 1
            x = i*j
    
primes = []    
for i in xrange(2,LIMIT):
    if is_prime[i]:
        primes.append(i)

#------------------------------------------------


k = 1
done = False
answer = 0
while not done:
    x = int(pow(k+1,3) - pow(k,3))
    if x > LIMIT:
        done = True
    else:
        if is_prime[x]:
            answer += 1
        k += 1

print answer