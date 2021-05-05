"""

Given an array nums of integers, return how many of them contain an even number of digits.


Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).
Therefore only 12 and 7896 contain an even number of digits.
Example 2:

Input: nums = [555,901,482,1771]
Output: 1
Explanation:
Only 1771 contains an even number of digits.


Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 10^5

"""

def is_num_even(num):

    # num_of_digit = 0
    # while num / 10 > 0:
    #     # print(num)
    #     num //= 10
    #     num_of_digit += 1
    # print(num_of_digit)
    number_string = str(num)
    print(number_string)
    num_of_digit = len(number_string)
    if num_of_digit%2 == 0:
        print(True)
        return True
    else:
        return False


# def is_num_even(num):
#     # print(num)
#     if num // 100000 > 0:
#         return True
#     if num // 10000 > 0:
#         # print('10000')
#         return False
#     if num // 1000 > 0:
#         # print('1000')
#         return True
#     if num // 100 > 0:
#         # print('100')
#         return False
#     if num // 10 > 0:
#         # print('10')
#         return True

def findNumbers(nums):
    even_digit_nums = 0
    for num in nums:
        if is_num_even(num):
            even_digit_nums += 1
    return even_digit_nums


if __name__ == '__main__':
    nums = [12, 345, 2, 6, 7896]
    print(findNumbers(nums))
    nums = [555,901,482,1771]
    print(findNumbers(nums))
    nums = [580,317,640,957,718,764]
    print(findNumbers(nums))