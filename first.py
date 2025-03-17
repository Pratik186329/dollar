def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series
n = int(input("Enter the number of terms: "))
fib_series = fibonacci(n)
print(f"Fibonacci series with {n} terms: {fib_series}")

