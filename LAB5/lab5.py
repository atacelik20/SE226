alt_sum = 0

def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)


term = lambda x, n: (x ** n) / factorial(n)


def exp_x(x, n):
    total = 0
    i = 0
    while i < n:
        total += term(x, i)
        i += 1
    return total


def alternating_series(n):
    global alt_sum

    if n == 0:
        return

    if n % 2 == 0:
        alt_sum -= 1 / n
    else:
        alt_sum += 1 / n

    alternating_series(n - 1)


x = float(input("Enter x value for e^x: "))
n = int(input("Enter n value for number of terms: "))

print("Factorial of", n, "=", factorial(n))
print("Approximation of e^x with", n, "terms =", exp_x(x, n))

n2 = int(input("Enter n value for alternating series: "))
alternating_series(n2)
print("Result of alternating series =", alt_sum)