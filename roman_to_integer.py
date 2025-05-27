
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
        result = 0
        n = len(s)
        
        for i in range(n):
            # Check if this character is followed by a larger character
            if i < n - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                result -= roman_map[s[i]]  # Subtract current value
            else:
                result += roman_map[s[i]]  # Add current value

        return result
    
c = Solution()
print("answer ")
print(c.romanToInt("MCMXCIV"))