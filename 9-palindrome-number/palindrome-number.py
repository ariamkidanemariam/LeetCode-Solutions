# Mathematical Mirror Trick
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and trailing zeros
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        
        # Store a copy of the original number before we modify x
        original_x = x
        current = 0
        
        # Process every single digit until x hits 0
        while x > 0:
            new_digit = x % 10
            current = current * 10 + new_digit
            x = x // 10  
            
        # Check if the fully reversed number matches the original copy
        return current == original_x


# Halfway Trick (Slicing the number exactly down the middle and comparing the left half to a flipped version of the right half. If they match, the number is a palindrome.)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and trailing zeros
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        
        current = 0 

        # Stop moving digits the exact moment the Reversed Pile 
        # becomes equal to or larger than the remaining Original Pile (x)
        while x > current:
            new_digit = x % 10
            current = current * 10 + new_digit
            x = x // 10 
            # Shave off the last digit from the Original Pile
            
        # Final Comparison
        # Even length: x == current 
        # Odd length:  x == current // 10 
        return x == current or x == (current // 10)