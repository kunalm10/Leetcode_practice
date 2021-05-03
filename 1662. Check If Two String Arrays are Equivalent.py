"""

Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.



Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true


Constraints:

1 <= word1.length, word2.length <= 103
1 <= word1[i].length, word2[i].length <= 103
1 <= sum(word1[i].length), sum(word2[i].length) <= 103
word1[i] and word2[i] consist of lowercase letters.

"""


def arrayStringsAreEqual(word1, word2):
    word1_string = ""
    word2_string = ""

    for string in word1:
        word1_string += string
        # print(word1_string)
    for string in word2:
        word2_string += string
        # print(word2_string)
    if word1_string == word2_string:
        return True
    else:
        return False


if __name__ == '__main__':
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    print(arrayStringsAreEqual(word1, word2))
    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    print(arrayStringsAreEqual(word1, word2))
    word1 = ["abc", "d", "defg"]
    word2 = ["abcddefg"]
    print(arrayStringsAreEqual(word1, word2))
