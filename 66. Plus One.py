"""

Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Example 3:

Input: digits = [0]
Output: [1]


Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9

"""


# def plusOne(digits):
#     n = len(digits)
#     for i in range(1,n+2):
#         if i < n+1:
#             if digits[-i] + 1 < 10:
#                 digits[-i] += 1
#                 break
#             else:
#                 digits[-i] = 0
#         else:
#             digits.insert(0, 1)
#     return digits


def plusOne(digits):
    return_digit = []
    for i, num in enumerate(digits[::-1]):
        if num + 1 < 10:
            return_digit = [num + 1] + return_digit
            break
        else:
            return_digit = [0] + return_digit
    if len(return_digit) < len(digits):
        return_digit = digits[:-(i + 1)] + return_digit
    else:
        if return_digit[0] == 0:
            return_digit.insert(0, 1)
    return return_digit


if __name__ == '__main__':
    digits = [9, 9, 9, 9]
    print(plusOne(digits))
    digits = [0]
    print(plusOne(digits))
    # plusOne(digits)
    # print(digits)
