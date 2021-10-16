# Write a function that takes a string and returns if the string is a palindrome.

def isPalidromeString(string):

    # step 3: validate input
    assert len(string) >=1 and type(string) == str
    
    
    # step 2: base condition - stopping criterion
    n = len(string)
    if n == 1:
        return string[0]
    else:
        # step 1: recursive case (flow)
        return string[n-1] + isPalidromeString(string[ :n-1])
    


print('Find Palindrome String\n')

user_input = input('Enter a string to check if it is a palindrome: ')
isPalindrome = isPalidromeString(user_input)
if isPalindrome == user_input:
    print(f'{user_input} is a palindrome: {isPalindrome}\n')
else:
    print(f'{user_input} is not a palindrome: {isPalindrome}\n')
