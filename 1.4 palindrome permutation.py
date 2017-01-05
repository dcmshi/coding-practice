'''
1.4 Palindrome Permutation
given a string, check if it is a permutation of a palindrome
'''

def palindrome_perm(input_str):
    no_spaces = ''.join(input_str.split())
    char_array = [0]*26
    for char in no_spaces:
        char_array[ord(char)-97]+=1
    num_odd = 0
    for i in range(0, 26):
        if char_array[i]%2==1:
            num_odd += 1
    if num_odd > 1:
        return False
    return True

print palindrome_perm('tact coa')
        
