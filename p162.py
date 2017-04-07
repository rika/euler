#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Para resolver o problema, utilizei o princípio da inclusão e exclusão:
https://en.wikipedia.org/wiki/Inclusion-exclusion_principle
"""

memo = {}

# função auxilar que guarda e recupera resultados já calculados
def calc(digits, func):
    name = func.__name__
    if name in memo:
        if digits in memo[name]: 
            return memo[name][digits]
    else:
        memo[name] = {}
    
    memo[name][digits] = func(digits)
    #print '  ', name, digits, memo[name][digits]
    return memo[name][digits] 

"""
O parametro n das funções abaixo representam a quantidade de dígitos.
Casos com zero são tratados diferente, pois o zero não pode ser o primeiro
dígito.
"""

# A função power da biblioteca math estava aproximando o resultado para valores
# muito grandes, então implementei a minha função power
def pow(x, n):
    t = x
    for i in xrange(n-1):
        t *= long(x)
    return t

# |T|
# total de números
def total(n):
    return long(15 * pow(16, n-1))

# |not Z|
# números com nenhum zero
def no_zero(n):
    return long(pow(15, n))

# |Z| = |T| - |not Z|
# números com pelo menos um zero
def at_least_one_zero(n):
    return calc(n, total) - calc(n, no_zero) 

# |not X|
# números com nenhum x>0
def no_x(n):
    return long(14 * pow(15, n-1))

# |X| = |T| - |not X|
# números com pelo menos um x>0
def at_least_one_x(n):
    return calc(n, total) - calc(n, no_x)

# |not (X or Y)|
# números com nenhum x>0 E nenhum y>0 
def no_x_and_no_y(n):
    return long(13 * pow(14, n-1))

# |X or Y| = |T| - |not (X or Y)|
# números com pelo menos um x>0 OU um y>0
def at_least_one_x_or_one_y(n):
    return calc(n, total) - calc(n, no_x_and_no_y)

# |X and Y| = |X| + |Y| - |X or Y|
# números com pelo menos um x>0 E pelo menos um y>0
def at_least_one_x_and_one_y(n):
    return 2*calc(n, at_least_one_x) - calc(n, at_least_one_x_or_one_y)

# |not (X or Z)|
# números com nenhum x>0 E nenhum zero
def no_x_and_no_zero(n):
    return long(pow(14, n))

# |X or Z| = |T| - |not (X or Z)|
# números com pelo menos um x>0 OU um zero
def at_least_one_x_or_one_zero(n):
    return calc(n, total) - calc(n, no_x_and_no_zero)

# |X and Z| = |X| + |Z| - |X or Z|
# números com pelo menos um x>0 E pelo menos um zero
def at_least_one_x_and_one_zero(n):
    return calc(n, at_least_one_x) + calc(n, at_least_one_zero) - calc(n, at_least_one_x_or_one_zero)

# |not (X or Y or Z)|
# números com nenhum x>0 E nenhum y>0 E nenhum zero
def no_x_and_no_y_and_no_zero(n):
    return long(pow(13, n))

# |X or Y or Z| = |T| - |not (X or Y or Z)| 
# números com pelo menos um x>0 OU um y>0 OU um zero
def at_least_one_x_or_one_y_or_one_zero(n):
    return calc(n, total) - calc(n, no_x_and_no_y_and_no_zero)

# |X and Y and Z| = |X or Y or Z| - |X| - |Y| - |Z| + |X and Y| + |X and Z| + |Y and Z|
# números com pelo menos um x>0 E pelo menos um y>0 E pelo menos um zero
def at_least_one_x_and_one_y_and_one_zero(n):
    return calc(n, at_least_one_x_or_one_y_or_one_zero) \
        - 2*calc(n, at_least_one_x) - calc(n, at_least_one_zero) \
        + calc(n, at_least_one_x_and_one_y) \
        + 2*calc(n, at_least_one_x_and_one_zero)


"""
Depois de prearar essas funções basta calcular a soma da quantidade de números
possíveis para digitos de 3 à 16.
"""
sum = 0
for i in xrange(3,17):
    x = at_least_one_x_and_one_y_and_one_zero(i)
    #print "%d: %d (%X)" % (i, x, x)
    sum += x
print format(sum, 'x').upper()
