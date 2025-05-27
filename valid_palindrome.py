"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward.
It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:
Input: s = "Was it a car or a cat I saw?"
Output: true
"""

def valid_palindrome(s: str) -> bool:
    # strip string of symbols and spaces
    char_array = [char for char in s if char.isalnum()]

    l = 0
    r = len(char_array) - 1
    print("in the function")

    while l < r:
        if char_array[l].lower() == char_array[r].lower():
            print("before increment")
            print("char_array[l]: " + char_array[l])
            l += 1
            print("----------------------------")
            print("before increment")
            print("char_array[r]: " + char_array[r])
            r -= 1
            print("----------------------------")
            print(l)
            print(r)


        elif char_array[l].lower() != char_array[r].lower():
            return False
    return True


def isPalindrome(self, s: str) -> bool:
        # make character array of string by adding each char to an array if it is a valid character
        char_array = [char for char in s if char.isalnum()]

        l = 0
        # place first pointer at front of array
        r = len(char_array) - 1
        # place second pointer at end of array

        # loop through character array until the characters do not match each other
        # if the characters match we increment/decrement pointers bringing them closer 
        # to the middle of the list
        """
        s = "racecar"

        l = 0
        char_array[l] (aka char_array[0]) = 'r'
        ------------------------------------------
        r = len(s)
        the length of the string is 8
        we want to start at 7 because s[8] will throw us out of bounds (IndexError)
        so we subtract one to stay in bounds
        r = len(s) - 1
        8-1=7
        s[7] = 'r'
        ----------------------------------------------
        write conditional statements to determine if we increment or decrement
        (use .lower so we can compare letters, using == is case sensitive)
        if char_array[l].lower() == char_array(r).lower():
            this reads if the letter at the index l(0 on our first iteration and we know it is 'r') is equal to the letter at the index r(which is 7 on the first iteration and we know that it is 'r' as well)
            since this is the same letter, it is a good thing and we can move our pointers closer to the middle
            so we increment l to move it to the right 
            l += 1
            now l = 1
            l -= 1
            now r = 6 and on the next loop we check if
            char[1] == char[6] so on and so forth until they do not equal each other or until l is the same number as r
            elif char_array[l].lower() != char_array(r).lower():
                if the letters do not equal each other it is not a palindrome
                return False
            return True
        """
        while l < r:
            if char_array[l].lower() == char_array[r].lower():
                l += 1
                r -= 1
            elif char_array[l].lower() != char_array[r].lower():
                return False
        return True

s = "race a car"
char_array = [char for char in s if char.isalnum()]
print(valid_palindrome(s))
print(char_array)
print(char_array[0])
print(char_array[-1])
string = "racecar"
