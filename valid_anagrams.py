
def valid_anagrams(s, t):
    hm = {}

    for letter in s:
        if letter not in hm:
            hm[letter] = 1
        hm[letter] += 1
        print("hm[letter]: ",hm[letter])

    print("end of first loop")

    for letter in t:
        if letter not in hm:
            return False
        hm[letter] -= 1
        print("hm[letter]: ",hm[letter])
        if hm[letter] < 0:
            return False
        
    for value in hm.values():
        print("value: ", value)
        
    
    
    return True

s = "racecar"
t = "carrace"

print(valid_anagrams(s, t))
