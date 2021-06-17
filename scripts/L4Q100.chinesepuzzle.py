'''
Write a program to solve 
a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens 
and rabbits in a farm. 
How many rabbits and how many chickens do we have?
'''

# i+j = 35
# and i*4 + j*2 = 94

# way 1:

from sympy import symbols, Eq, solve

import time
start = time.time()

rabbit, chicken = symbols('rabbit chicken')
eq1 = Eq(rabbit+chicken-35)
eq2 = Eq(4*rabbit + 2*chicken -94)
sol = solve((eq1, eq2), (rabbit,chicken))

end = time.time()
print(sol)
print(round(end-start, 2))

# way 2:


def solve(nheads,nlegs):
    ns='No solutions!'
    for i in range(nheads+1):
        j=nheads-i
        if 2*i+4*j==nlegs:
            return f'chicken: {i}  and rabbit: {j}'
    return ns

nheads=35
nlegs=94
solutions=solve(nheads,nlegs)
print(solutions)


