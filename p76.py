"""
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
"""


x = 100

p = {}

for n in xrange(2,x+1):
    sum = 0
    s = ""
    for k in xrange(1,n+1):
        if k in [1,n]:
            p[(n,k)] = 1
        elif k <= n-k:
            p[(n,k)] = p[(n-1,k-1)] + p[(n-k),k]
        else:
            p[(n,k)] = p[(n-1,k-1)]
        sum += p[(n,k)]
        s += " "+str(p[(n,k)])
    print "(%3d): %3d | %s" % (n, sum, s)

        
