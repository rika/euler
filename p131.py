#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt, pow

LIMIT = 1000000

#------------------------------------------------
"""
Encontrando primos até 1000000
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

is_prime[x] devolve se x é primo ou não
"""

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

#------------------------------------------------
"""
Algumas contas para resolver o problema:

n³ + n²p = x³
=> n²(n+p) = x³

Daqui para termos um cubo perfeito, n e n+p devem ser cubos perfeitos também,
senão n+p = n² para formar um cubo perfeito que é um absurdo.

n = a³
n+p = b³

=> p = b³ - a³ = (a - b)(a² + ab + b²)

Como p é primo ele não pode ser um produto então um dos fatores é 1.
Como a²>=1 e b²>=1, temos que (a² + ab + b²) > 1 e (a-b) = 1.

b = a + 1

Dado que p = b³ - a³, temos que p é a diferença de cubos "vizinhos".
"""

# Testando primalidade de todas as diferenças de cubos "vizinhos" até 1000000
# chegamos à resposta 173
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