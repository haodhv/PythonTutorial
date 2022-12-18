def giai_thua(n):
    if n == 0:
        return 1
    else:
        return giai_thua(n - 1) * n


def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n-1)
