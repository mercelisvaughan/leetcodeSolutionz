"""

Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold
the additional characters, and that you are given the "true"
length of the string

"""

def urlify(s) -> str:

    s = "hello"
    char_array = list(s)

    for i in range(len(char_array)):
        if char_array[i] == " ":
            char_array[i] = '%20'
    
    return "".join(char_array)