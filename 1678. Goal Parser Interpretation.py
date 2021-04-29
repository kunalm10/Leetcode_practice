"""
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.



Example 1:

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
Example 2:

Input: command = "G()()()()(al)"
Output: "Gooooal"
Example 3:

Input: command = "(al)G(al)()()G"
Output: "alGalooG"


Constraints:

1 <= command.length <= 100
command consists of "G", "()", and/or "(al)" in some order.
"""

import time


def interpret(command):
    parser_dict = {'G': 'G', '()': 'o', '(al)': 'al'}
    chars = parser_dict.keys()
    print(chars)
    output = ""
    # print(command[0:1])

    starting_index = 0
    ending_index = 1
    # print(f'len(command) = {len(command)}')
    while starting_index != len(command):
        while command[starting_index:ending_index] not in parser_dict.keys():
            # print(f'command[{starting_index}: {ending_index}] = {command[starting_index: ending_index]}')
            ending_index += 1
            time.sleep(1)
        # print(f'command[{starting_index}: {ending_index}] = {command[starting_index: ending_index]}')
        output += parser_dict[command[starting_index: ending_index]]
        print(f'{output}\n')
        starting_index = ending_index

    # for char in chars:
    #     if char in command:
    #         print(command.index(char))
    # command.index(char) = parser_dict[char]
    # command[command.index(char)] = parser_dict[char]
    return output


if __name__ == '__main__':
    # command = "G()(al)"
    # print(interpret(command))
    command = "G"
    print(interpret(command))
