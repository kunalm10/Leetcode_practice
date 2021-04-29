"""

Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.



Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
Example 4:

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'


Constraints:

1 <= s.length <= 1000
s[i] is either 'L' or 'R'.
s is a balanced string.

"""

def balancedStringSplit(s):
    output = 0
    s_i = 0
    while s_i != len(s):
        index = s_i
        count_dict = {'L': 0, 'R': 0}
        # print(index)
        # print(count_dict['L'])
        while (count_dict['L'] != count_dict['R']) or count_dict['L'] == 0 or count_dict['R'] == 0:
            # print(s[index])
            if s[index] == 'L':
                count_dict['L'] += 1
            else:
                count_dict['R'] += 1
            index += 1
            # print(index)
        output += 1
        s_i = index
        # print(f's_i = {s_i}')
    return output


if __name__ == '__main__':

    s = "RLRRLLRLRL"
    print(balancedStringSplit(s))
    s = "RLLLLRRRLR"
    print(balancedStringSplit(s))
    s = "LLLLRRRR"
    print(balancedStringSplit(s))
    s = "RLRRRLLRLL"
    print(balancedStringSplit(s))
