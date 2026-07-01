
def twoSum(numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1

    while left < right:
        currentSum = numbers[left] + numbers[right]
        if currentSum == target:
            return [left+1, right+1]
        elif currentSum > target:
            right -= 1
        else:
            left += 1

numbers = [2,7,11,15]
target = 9

print(twoSum(numbers, target))