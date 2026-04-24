def fibonacci(n):
    if n <= 1: 
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print("Dãy Fibonacci:")
for i in range(10):
    print(fibonacci(i), end=" ")