def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example usage:
num_terms = 10
print(f"Fibonacci series up to {num_terms} terms: {fibonacci(num_terms)}")
