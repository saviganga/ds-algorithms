# Write a recursive function that takes a list of numbers as an input and returns the product of all the numbers in the list.

def calcProdList(arr):

    # validate input
    assert len(arr) >= 1, 'Array must contain values'

    # step 2: base condition - stopping criterion
    if len(arr) == 1:
        return arr[0]

    # step 1: recursive case (flow)
    return arr[0] * calcProdList(arr[1:])


print('Calculate the product of all numbers in an array\n')
user_input = input('Enter a sequence of numbers seperated by space: ')

num_list = user_input.split(' ')
while '' in num_list:
    num_list.remove('')
num_list = list(map(int, num_list))

prodList = calcProdList(num_list)
print(f'The product of all numbers in the sequence {user_input}: {prodList}')
