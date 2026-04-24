def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n_test = 7
ket_qua = fibonacci(n_test)

print(f"Số Fibonacci thứ {n_test} là: {ket_qua}")
