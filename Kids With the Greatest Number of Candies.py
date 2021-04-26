# 1431


def kidsWithCandies(candies, extraCandies):
    output = list()
    max_number = max(candies)

    for kid_candies in candies:
        if kid_candies + extraCandies >= max_number:
            output.append('true')
        else:
            output.append('false')
    return output


if __name__ == '__main__':
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    print(kidsWithCandies(candies, extraCandies))
