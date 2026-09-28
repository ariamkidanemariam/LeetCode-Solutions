class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        # Initialize the counter to track symmetric numbers
        count = 0
        
        # Loop through each number in the range from low to high inclusive
        for i in range(low, high + 1):
            num_str = str(i)  
            # Convert the number to a string to check its length
            
            # Check if the number has an even length
            if len(num_str) % 2 == 0:
                # Find the middle index to split the string
                mid = len(num_str) // 2
                
                # Slice the string from the start to the middle point
                first_half = num_str[:mid] 
                
                # Slice the string from the middle point to the very end
                last_half = num_str[mid:]

                # Summing the individual digits of the first half
                sum_first = 0
                for char in first_half:
                    sum_first = sum_first + int(char) 

                # Summing the individual digits of the last half
                sum_last = 0
                for char in last_half:
                    sum_last = sum_last + int(char) 
                
                # Check if the sum of the first half matches the sum of the last half
                if sum_first == sum_last:
                    count += 1  # Add 1 to our running total if it is a symmetric number
        
        # Return the final amount of symmetric numbers found
        return count
