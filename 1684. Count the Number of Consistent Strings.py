"""

You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.



Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.
Example 3:

Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.


Constraints:

1 <= words.length <= 104
1 <= allowed.length <= 26
1 <= words[i].length <= 10
The characters in allowed are distinct.
words[i] and allowed contain only lowercase English letters.

"""


# Method 1
# def countConsistentStrings(allowed, words):
#     # allowed_list = [allowed_alpha for allowed_alpha in allowed]
#     # print(allowed_list)
#     output = 0
#     for word in words:
#         length_word = len(word)
#         for index, char in enumerate(word):
#             if char not in allowed:
#                 break
#             else:
#                 if index + 1 == length_word:
#                     output += 1
#     return output


# Method 2
def countConsistentStrings(allowed, words):
    count = 0
    for i in words:
        for l in i:
            if l not in allowed:
                count -= 1
                break
        count += 1
    return count


if __name__ == '__main__':
    allowed = "ab"
    words = ["ad","bd","aaab","baa","badab"]
    print(countConsistentStrings(allowed, words))