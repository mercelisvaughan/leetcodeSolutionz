"""

Given two strings, write a method to decide if one is a permutation of the other

This is basically the same question as valid anagrams

"""

def check_permutation(s1, s2) -> bool:
    hm = {}

    if len(s1) != len(s2):
        return False
    
    for character in s1:
        if character not in hm:
            hm[character] = 1
        else:
            hm[character] += 1

    for character in s2:
        if character not in hm:
            return False
        hm[character] -= 1

    for value in hm.values():
        if value != 0:
            return False



    return True