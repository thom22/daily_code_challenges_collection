# Recursive problem
'''
Given an integer x, return true if x is apalindrome, and false otherwise.
Ex. 
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
'''

# Answer 

# class Solution:
def isPalindrome(x: int):
    
    # if the number is less than it always not palindrome
    if x < 0:
        return False

    number = x # define the number in a var
    reverse = 0 # store the reverse no
    while number:
        reverse = reverse * 10 + number % 10
        number //= 10
    return x == reverse