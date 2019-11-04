def sum(*numbers):
    if len(numbers) == 0:
        return 0
    else:
        acc = numbers[0] + sum (*numbers[1:])
        print(acc,numbers)
        return acc


def fib(n : int) -> int:
    if n <= 2:
        return 1
    return fib(n -2) + fib(n -1)
