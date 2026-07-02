from typing import List

def maxArea(heights: List[int]) -> int:
    maxVolume = 0
    left = 0
    right = len(heights) - 1


    # remember base * height and ask yourself what numbers
    # do you want to keep track of in the conditional loop

    while left < right:
        width = right - left
        currentHeight = min(heights[left], heights[right])
        currentVolume = width * currentHeight
        maxVolume = max(maxVolume, currentVolume)
        
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return maxVolume

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
#Indices: 0  1  2  3  4  5  6  7  8