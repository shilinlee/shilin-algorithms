def t2b_fibonacci(n):
    """
    0ms
    top to bottom of fib
    """
    if n <= 0:
        return n

    memo = []

    for i in range(n+1):
        memo.append(-1)

    return fib(n, memo)


def fib(n, memo):
    """
    :param n:
    :param memo:
    :return:
    """

    if memo[n] != -1:
        return memo[n]

    if n <= 2:
        memo[n] = 1
    else:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)

    return memo[n]


if __name__ == '__main__':
    print(t2b_fibonacci(6))
    print(t2b_fibonacci(100))
