def two_sum(nums, target):
    # Create a dictionary to store the numbers we've seen and their indices
    num_dict = {}

    # Iterate through the list of numbers
    for i, num in enumerate(nums):
        # Calculate the complement (the number we need to find to make the pair)
        complement = target - num

        # Check if the complement exists in the dictionary
        if complement in num_dict:
            # If it does, return the current index and the index of the complement
            return [num_dict[complement], i]

        # If not, add the current number and its index to the dictionary
        num_dict[num] = i

    # If no solution found, return an empty list (based on the problem statement, this shouldn't occur)
    return []

# Testing the function
nums = [2, 7, 11, 15, 1, 8]
target = 9
print(two_sum(nums, target))  # Expected output: [0, 1]
