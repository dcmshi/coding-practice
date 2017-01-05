'''
1.1 Is Unique
determine if a string has all unique characters.
What if you cannot use additional data structures?
'''

def is_unique(input_str):
    char_arr = [0] * 26
    for char in input_str:
        char_arr[ord(char)-97]+=1

    for count in char_arr:
        if count > 1:
            return False
    return True

def is_unique_nostructure(input_str):
    sorted_str = ''.join(sorted(input_str))
    for i in range(0, len(sorted_str)-1):
        if sorted_str[i] == sorted_str[i+1]:
            return False
    return True
                         
print is_unique('lol')
print is_unique_nostructure('lol')
print is_unique('abcdefghijklmnopqrstuvwxyz')
print is_unique_nostructure('abcdefghijklmnopqrstuvwxyz')
