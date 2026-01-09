def findTheDifference(s: str, t: str) -> str:
        hm = {}

        for letter in s:
            if letter not in hm:
                hm[letter] = 1
            else:
                 hm[letter] += 1

        for letter in t:
            if letter not in hm:
                  return letter

            hm[letter] -= 1

            if hm[letter] < 0:
                return letter

"""

we are looking for the difference in the first string and the second

how do we find that with a dictionary


"""