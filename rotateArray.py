def rotateArray(arr, positions):

    d = d % len(arr) # basically we're shifting by the remainder
    

    return arr[d:] + arr[:d]
    

#rotateArray([1,2,23,4], 3)
