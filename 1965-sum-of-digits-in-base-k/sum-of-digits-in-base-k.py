class Solution:
    def sumBase(self, n: int, k: int) -> int:
        # Initialize a running total to store the sum of the base-k digits
        total = 0 

        # Loop until all digits have been extracted and n becomes 0
        while n > 0:
            
            # Isolate the rightmost digit of n in base k using the modulo operator
            remainder = n % k

            # Add the extracted digit directly to our running sum
            total += remainder

            # Remove the rightmost digit from n using integer division to prepare for the next loop
            n = n // k

        # Return the final sum after the loop has completely processed all digits
        return total
