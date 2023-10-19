# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# Rotate 1 steps to the right: [7,1,2,3,4,5,6]
# Rotate 2 steps to the right: [6,7,1,2,3,4,5]
# Rotate 3 steps to the right: [5,6,7,1,2,3,4]


def rotate(nums, k):
    n = len(nums)
    k %= n  # handle cases where k > n

    
    # Helper function to reverse a portion of the array
    def reverse(start, end):
        

        while start < end:
            print("Start is : ",start)
            print("End is : ",end)
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    # Reverse entire array
    reverse(0, n-1)
    
    # Reverse the first k elements
    #reverse(0, k-1)
    
    # Reverse the remaining elements
    #reverse(k, n-1)



# Test
nums = [1,2,3,4,5,6,7]
k = 1
rotate(nums, k)
print(nums)  # Expected output: [5,6,7,1,2,3,4]
