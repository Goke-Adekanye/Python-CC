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


# print(max_sub_array([-1, 2, -3, 3, 5]))


# CHECK FIBONACCI
def is_fibonacci(arr):
    if len(arr) < 3:
        return False

    for i in range(len(arr) - 2):
        if arr[i] + arr[i + 1] != arr[i + 2]:
            return False

    return True


# print(is_fibonacci([1, 1, 2, 3, 5, 8, 13]))  # true
# print(is_fibonacci([1, 1, 2, 3, 4, 8, 13]))  # false


# CREATE FIBONACCI
def create_fibonacci(num):  # 1
    if num < 3:
        return False
    stack = [1]

    for i in range(num - 2):
        if len(stack) == 1:
            stack.append(i + 1)
        stack.append(stack[i] + stack[i + 1])

    return stack


# print(create_fibonacci(5))


# FIND FACTORIAL
def find_factorial(num):  # 1
    factorial = 1
    # Loop from 'num' down to 1, decrementing by 1 in each iteration
    for i in range(num, 0, -1):
        factorial *= i

    return factorial


def find_factorial(num):  # 2
    if num == 0 or num == 1:
        return 1
    else:
        factorial = num * find_factorial(num - 1)
        return factorial


# print(find_factorial(5))


# REMOVE ELEMENT
def remove_element(arr, element):
    stack = []
    for i in range(len(arr)):
        if arr[i] != element:
            stack.append(arr[i])

    return stack


def remove_element(arr, element, option=False):
    if option:
        # Use filter() to include only the items in 'arr' that are not equal to 'element'
        # Convert the result of filter() back into a list
        return list(filter(lambda item: item != element, arr))
    else:
        # Create a new list that includes only the items in 'arr' that are not equal to 'element'
        return [item for item in arr if item != element]


# print(remove_element([1, 2, 5, 2, 3, 7], 3))


# REMOVE DUPLICATES
def remove_duplicates(arr, option):
    stack = []

    if option == "first":
        for i in range(len(arr)):
            if arr[i] not in stack:
                stack.append(arr[i])

    elif option == "second":
        i = 0
        while i < len(arr):
            if arr[i] not in stack:
                stack.append(arr[i])
            i += 1

    else:
        # Use a set to keep track of seen elements
        seen = set()
        # Use filter() to create a new list with unique elements
        # The lambda function checks if the item is not in the set and adds it if it's new
        return list(filter(lambda x: x not in seen and not seen.add(x), arr))
        # Explanation of 'x not in seen and not seen.add(x)':
        # 1. 'x not in seen' checks if x is not in the set
        # 2. 'and not seen.add(x)' does two things:
        #    a) Adds x to the set (side effect)
        #    b) Always evaluates to True (because set.add() returns None, and 'not None' is True)
        # 3. If x is already in seen, the first part is False, so the second part isn't evaluated
        #    (short-circuit evaluation), and x isn't added again
        # 4. This 'trick' allows us to check for uniqueness and update seen items in one expression
    return stack


print(remove_duplicates([1, 2, 2, 3, 5, 5, 7], ""))
