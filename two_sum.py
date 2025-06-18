

def two_sum(arr, target):
    hm = {}
    for index, value in enumerate(arr):
        complement = target - value
        if complement in hm:
            return [hm[complement], index]
        hm[value] = index
    return []