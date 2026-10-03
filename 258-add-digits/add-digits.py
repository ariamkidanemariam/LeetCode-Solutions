class Solution:
    def addDigits(self, num: int) -> int:
        # Step 1: Handle the absolute zero edge case first
        if num == 0:
            return 0
            
        # Step 2: Apply your remainder logic
        if num % 9 != 0: 
            total_digits = num % 9 
        else: 
            total_digits = 9  
            
        # Step 3: Return the variable you calculated
        return total_digits
    

class Solution:
    def addDigits(self, num: int) -> int:
        # Keep going until num is a single digit (0 to 9)
        while num >= 10:
            current_sum = 0
            
            # Strip digits from num and add them to current_sum
            while num > 0:
                digit = num % 10
                current_sum += digit
                num = num // 10
            
            # Reset num to be the new sum for the next round of the outer loop
            num = current_sum
            
        return num

