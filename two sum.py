# 1480


# def runningSum(self, nums: list[int]) -> list[int]:
def runningSum(nums):
    output_list = []

    for i, num in enumerate(nums):
        if i == 0:
            output_list.append(num)
        else:
            print(output_list[i - 1])
            next_num = output_list[i - 1] + num
            output_list.append(next_num)
    return output_list


def csac(nums):
    lst = []
    num = 1
    while len(lst) != len(nums):
        lst.append(sum((nums[0:num])))
        num += 1
    return lst


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(csac(nums))
    print(runningSum(nums))
