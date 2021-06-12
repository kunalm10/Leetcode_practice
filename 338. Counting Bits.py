"""

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.



Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101


Constraints:

0 <= n <= 105

"""

def binaryRepresentationFunction(num):
    number = num
    number_of_bits_required = 0
    binary_representation_string = ''
    number_of_ones_in_bit_representaion_string = 0
    if num == 0:
        binary_representation_string = 0
        return binary_representation_string
    while num >= 1:
        num //= 2
        number_of_bits_required += 1

    for i in range(number_of_bits_required, 0, -1):
        # print(2**(i-1))
        if number >= 2 ** (i-1):
            number -= 2 ** (i-1)
            binary_representation_string = binary_representation_string + '1'
            number_of_ones_in_bit_representaion_string += 1
        else:
            binary_representation_string = binary_representation_string + '0'

    return number_of_ones_in_bit_representaion_string

class Solution:
    def countBits(n):
        output_array = []
        for i in range(n+1):
            output_array.append(binaryRepresentationFunction(i))
        return output_array

print(Solution.countBits(5))