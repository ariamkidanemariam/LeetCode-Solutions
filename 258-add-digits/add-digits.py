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
    


