# VALID STRING
def is_valid(str):

    map = {
        "(": ")",
        "{": "}",
        "[": "]",
    }  # Dictionary to map opening brackets to their corresponding closing brackets
    stack = []  # Stack to keep track of opening brackets

    for char in str:  # Iterate through each character in the input string
        if char in map:  # If the character is an opening bracket
            stack.append(char)  # Push it onto the stack
        else:
            # Check if the stack is empty or if the current closing bracket
            # doesn't match the most recent opening bracket
            if not stack or map[stack.pop()] != char:
                return False

    return len(stack) == 0


# print(is_valid("[(()){{}}]"))


# TWO SUM
def two_sum(arr, val):
    obj = {}  # Dictionary to store numbers and their indices

    for i in range(len(arr)):  # Iterate through the array
        # Calculate the complement (the number needed to reach val)
        complement = val - arr[i]
        if complement in obj:  # Check if the complement exists in our dictionary
            # If found, return the indices of the complement and current number
            return [obj[complement], i]
        else:  # If not found, add the current number and its index to the dictionary
            obj[arr[i]] = i

    return []


# print(two_sum([2, 7, 8, 5, 6], 13))


# MAXIMUM SUBARRAY SUM
def max_sub_array(arr):
    if len(arr) == 1:
        return arr[0]

    # Note: round() to the nearest even integer when the fractional part is exactly 0.5.
    m = round(len(arr) / 2)

    # Recursively find the maximum subarray sum in the left half and right half
    left_mss = max_sub_array(arr[:m])
    right_mss = max_sub_array(arr[m:])

    left_sum = -(2**53) + 1
    right_sum = -(2**53) + 1
    sum = 0

    # Iterate through the right half of the array starting from index 'm' to the end.
    for i in range(m, len(arr)):
        sum += arr[i]
        right_sum = max(right_sum, sum)

    sum = 0

    # Iterate through the left half of the array in reverse (from 'm-1' down to '0').
    for i in range(m - 1, -1, -1):
        sum += arr[i]
        left_sum = max(left_sum, sum)

    # Calculate the maximum subarray sum either from the left half, right half, or across both halves.
    ans = max(left_mss, right_mss)
    return max(ans, left_sum + right_sum)


print(max_sub_array([-1, 2, -3, 3, 5]))
