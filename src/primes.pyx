# cython: language_level=3
def find_primes_cython(int N):
    cdef int num, i, is_prime
    primes = []  # No need to use cdef for a Python list

    for num in range(2, N+1):
        is_prime = 1
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                is_prime = 0
                break
        if is_prime:
            primes.append(num)

    return primes
