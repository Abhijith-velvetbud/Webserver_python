def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci_recursive(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq

# Example usage:
num_terms = 10
print(f"Fibonacci series up to {num_terms} terms: {fibonacci_recursive(num_terms)}")
