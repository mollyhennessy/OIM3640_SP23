# using .find

import sympy

pi = str(sympy.N(sympy.pi,500000))
print(pi[:500])
print("-" * 50)
# return index of where this pattern starts
print(pi.find('060202')