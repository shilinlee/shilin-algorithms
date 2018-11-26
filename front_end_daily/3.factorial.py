"""
计算阶乘
N! = n * (n-1) * (n-2) * … * 3 * 2 * 1

1<=N <= 100

给出n
计算n的阶乘
"""


def main(n):
    res = 1
    for i in range(2, n+1):
        res = res * i

    print("n的阶乘：", res)


if __name__ == '__main__':
    n = input("请输入一个数字:")
    main(int(n))