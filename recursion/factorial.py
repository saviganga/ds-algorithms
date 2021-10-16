
# use recursion to find the factorial of a number

def findFactorial(n):

    # step 3: validate data coming in
    assert n >= 0 and int(n) == n, 'Positive integers only'

    # step 2: base case - stopping criterion
    if n in [0, 1]:
        return 1
    else:

        # step 1: recursive case
        return n * findFactorial(n - 1)

print(findFactorial(10))