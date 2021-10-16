# write a function to calculate the sum of a list of numbers

def calcSumList(arr):

    # step 3: validate input
    assert len(arr) >= 1, 'List must contain values'

    # step 2: base condition - stoppng criterion
    if len(arr) == 1:
        return arr[0]
    else:

        # step 1: recursive flow
        return arr[0] + calcSumList(arr[1:])


user_input = input('Enter a list of numbers seperated by space: ')
num_list = user_input.split(' ')
print(num_list)
while '' in num_list:
    num_list.remove('')
print(num_list)
num_list = list(map(int, num_list))
listSum = calcSumList(num_list)
print(f'The sum of all numbers in the sequence {user_input}: {listSum}')