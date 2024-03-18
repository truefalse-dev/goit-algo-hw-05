def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        """
        :param n:
        :return:
        """
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci


def main():
    fib = caching_fibonacci()

    print(fib(10))
    print(fib(15))


if __name__ == "__main__":
    main()