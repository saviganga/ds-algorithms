# Write a recursive function that takes a string and reverse the string.

def reverseString(strng):

    # step 3: validate input
    assert len(strng) >=1 and type(strng) == str


    # step 2: base condition
    n = len(strng)
    if n == 1:
        return strng[0]
    else:
    
        # step 1: recursive case (flow)
        return strng[n - 1] + reverseString(strng[ :n-1])


print('Reverse a string\n')

user_input = input('Enter a string to reverse it: ')
reversedString = reverseString(user_input)
print(f'{user_input}: {reversedString}\n')