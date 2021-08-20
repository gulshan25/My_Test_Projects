def fibo(nth_term):
    first = 0
    second = 1
    for i in range(nth_term - 1):
        future = first + second
        first = second
        second = future

    return first


print(fibo(10000))