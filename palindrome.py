# A phrase is a palindrome if, 
# after converting all uppercase letters into lowercase letters and
# removing all non-alphanumeric characters,
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

def solution(string):
    
    #reversing the string
    revString = string[::-1] #or reversed(string)
    for n,m in zip(string, revString):
        if n != m:
            return False
    return True

    #using pointers
    i,j = 0, len(string)-1
    while i < j:
        if string[i] != string[j]:
            return False
        i,j = i+1, j-1
    return True

solution('amanaplanacanalpanama')