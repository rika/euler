#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Depois de quebrar a cabeça tentando achar a recurção que resolve o problema,
dei uma perguntada pro tio Google e achei isso aqui:
http://mathworld.wolfram.com/PartitionFunctionP.html

#------------------------------------------------------------------------------
...
P(n,k) denotes the number of ways of writing n as a sum of exactly k terms or,
equivalently, the number of partitions into parts of which the largest is
exactly k. (Note that if "exactly k" is changed to "k or fewer" and
"largest is exactly k," is changed to "no element greater than k," then the
partition function q is obtained.) For example, P(5,3)=2, since the partitions
of 5 of length 3 are {3,1,1} and {2,2,1}, and the partitions of 5 with maximum
element 3 are {3,2} and {3,1,1}.

The P(n,k) such partitions can be enumerated in the Wolfram Language using
IntegerPartitions[n,  {k}].

P(n,k) can be computed from the recurrence relation

P(n,k)=P(n-1,k-1)+P(n-k,k)     

(Skiena 1990, p. 58; Ruskey) with P(n,k)=0 for k>n, P(n,n)=1,
and P(n,0)=0. The triangle of P(k,n) is given by

1                      1
1  1                   2
1  1  1                3
1  2  1  1             5
1  2  2  1  1          7
1  3  3  2  1  1      11
...
#------------------------------------------------------------------------------

Tentando explicar:

P(n,k) é o número de jeitos de se escrever n com k termos.
Pelo que entendi podemos separá-lo em casos que contém o termo 1 e casos que não
contém o termo 1.

P(7,3)
5 1 1
4 2 1
3 3 1 contém 1
-----
3 2 2 não contém 1

Para casos que contém o termo um fazemos P(n-1, k-1) ou seja achamos como
escrever n-1 com um termo a menos.

P(6,2)
5 1
4 2
3 3 (iguais ao do P(7,3) sem o termo 1 no final)


Para casos que não contém o 1, é possível subtrair 1 de todos os termos, e assim
subtrair o número de termos (k) do total (n) e teremos uma combinação P(n-k,k)
que já foi calculada anteriormente.

P(4,3)
2 1 1 (somando 1 em cada termo voltamos à o caso que não contém 1 de P(7,3)) 

Então por isso a fórmula é:
P(n, k) = P(n-1, k-1) + P(n-k, k)

#------------------------------------------------------------------------------

P(100) = 190569292

Lembrando que temos que subtrair 1 por não estarmos contando o caso com 1 termo
para o problema.

Então a resposta é 190569291 
"""


x = 100

p = {}

for n in xrange(2,x+1):
    sum = 0
    for k in xrange(1,n+1):
        if k in [1,n]:
            p[(n,k)] = 1
        elif k <= n-k:
            p[(n,k)] = p[(n-1,k-1)] + p[(n-k),k]
        else: #k > n-k
            p[(n,k)] = p[(n-1,k-1)]
        sum += p[(n,k)]
print sum

        
