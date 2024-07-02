def fibonacci(n):
    # Initialize first two terms
    fib_series = [0, 1]
    
    # Generate Fibonacci sequence
    for i in range(2, n):
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
    
    return fib_series

# Example usage:
n = 10  # Number of terms in the Fibonacci series
result = fibonacci(n)
print(f"Fibonacci series up to {n} terms:", result)
