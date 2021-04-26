# 1672


def maximumWealth(accounts):
    wealth = [sum(person) for person in accounts]
    return max(wealth)


if __name__ == '__main__':
    accounts = [[1, 2, 3], [3, 2, 1]]
    print(maximumWealth(accounts))
