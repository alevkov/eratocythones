from primes import find_primes_cython
import timeit

def find_primes_python(N):
    primes = []
    for num in range(2, N+1):
        is_prime = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

    

def benchmark():
    N = 100000
    cython_time = timeit.timeit(lambda: find_primes_cython(N), number=1000)
    python_time = timeit.timeit(lambda: find_primes_python(N), number=1000)
    
    print(f"Cython time: {cython_time:.6f} seconds")
    print(f"Python time: {python_time:.6f} seconds")

benchmark()