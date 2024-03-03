import sympy

# The 150-bit number
n = 510143758735509025530880200653196460532653147

# Factorizing the number
factors = sympy.factorint(n)

# Getting the prime factors
prime_factors = list(factors.keys())

# The smaller prime factor
smaller_prime = min(prime_factors)
heigher_prime = max(prime_factors)

print("The smaller prime factor is:", smaller_prime)
print("The heigher prime factor is:", heigher_prime)

print(smaller_prime * heigher_prime == n)