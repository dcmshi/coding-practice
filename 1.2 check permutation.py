'''
1.2 check permutation
given two strings, decide if one is a permutation of the other
'''

def check_permutation(a, b):
    char_array_a = [0]*26
    char_array_b = [0]*26
    for char in a:
        char_array_a[ord(char)-97]+=1
    for char in b:
        char_array_b[ord(char)-97]+=1
    for i in range(0, 26):
        if char_array_a[i] != char_array_b[i]:
            return False
    return True

print check_permutation('artanis', 'starnia')
print check_permutation('bottle', 'throttle')
