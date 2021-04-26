#method 1
# def shuffle(nums, n):
#     mid = n
#     i = 0
#     ans = []
#
#     while i<n:
#         ans.append(nums[i])
#         i+=1
#         ans.append(nums[mid])
#         mid += 1
#     return ans

#method 2
def shuffle(nums, n):
    output_list = [0 for _ in range(2*n)]
    for i, num in enumerate(nums):
        if i < n:
            output_list[2 * i] = num
        else:
            output_list[2 * (i - n) + 1] = num
    return output_list

if __name__ == '__main__':
    nums = [2, 5, 1, 3, 4, 7]
    n = 3

    # assert shuffle(nums, n) == [2, 3, 5, 4, 1, 7]
    print(shuffle(nums, n))
