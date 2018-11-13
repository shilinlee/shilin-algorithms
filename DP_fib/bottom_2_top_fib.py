def b2t_fibonacci(n):
    """
    0ms
    bottom to top of fib
    """
    memo = []
    for i in range(n+1):
        memo.append(0)

    if len(memo) >= 2:
        memo[1] = 1

    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]


if __name__ == '__main__':
    print(b2t_fibonacci(6))
    print(b2t_fibonacci(100))
