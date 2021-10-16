# Write a recursive function that takes a number and returns the sum of all the numbers from zero to that number.

def findCumulative(n):

    # step 3: validate input
    assert n >= 0 and int(n) == n, 'Input must be positive integer'

    # step 2: base condition - stopping criterion
    if n == 0:
        return n

    # step 1: find recursive case (flow)
    return n + findCumulative(n - 1)


print('Calculate the cumulative of a number')
num = int(input('Enter a positive number: '))
numCumulative = findCumulative(num)
print(f'The Cumulative of {num}: {numCumulative}')