# use recursion to find fibonacci numbers

def findFibonacciNumber(n):

    # step 3: validate input
    assert n >= 0 and int(n) == n, 'Fibonacci numbers must be positive integers'

    # step 2: base condition - stopping criterion
    if n in [0, 1]:
        return n
    else:

        # step 1: recursive case (flow)
        return findFibonacciNumber(n - 1) + findFibonacciNumber(n - 2)


number = int(input('Enter a number to find its Fibonacci number: '))
fibNum = findFibonacciNumber(number)
print(f'Fibonacci number of {number}: {fibNum}')