#Given nums = [3, 7, 0, 1, 4, 2, 6,8,10],
#Return 5 because it's the missing number in the range 0 to 7.


def find_missing_num(number_array):
    output=[]
    number_array = sorted(number_array)
    print(number_array)
    for item in range(len(number_array)-1):
        if number_array[item+1] != number_array[item]+1:
            output.append(number_array[item]+1)
        else:
            continue
    return output
number_array = [3, 7, 0, 1, 4, 2, 6, 8, 10]
print(find_missing_num(number_array))



def find_missing_num(nums):
    nums_set = set(nums)
    n = max(nums)  # find the maximum value in the list
    
    # Check each number from 0 to n
    for i in range(n + 1):
        if i not in nums_set:
            return i
    
    return n + 1  # handle the case where the missing number is n + 1

number_array = [3, 7, 0, 1, 4, 2, 6, 8, 10]
print(find_missing_num(number_array))  # Expected output: 9

