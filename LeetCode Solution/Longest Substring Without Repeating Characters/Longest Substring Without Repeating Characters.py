class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        length_of_substring = 0
        longest_length = 0
        for sub in s:
            if substring == "":
                substring = sub
                length_of_substring += 1
            else:
                if sub in substring :
                    if longest_length < length_of_substring:
                         longest_length = length_of_substring
                    index_repeated_character = substring.find(sub)
                    new_substring = ""
                    print(index_repeated_character)
                    for index_substring in range((index_repeated_character+1),len(substring)):
                            new_substring = new_substring + substring[index_substring]
                    substring = new_substring + sub
                    length_of_substring = len(substring)
                else:
                    substring = substring + sub
                    length_of_substring += 1
                    length_of_substring = len(substring)
                    print(substring)
            if longest_length < length_of_substring:
                         longest_length = length_of_substring
        return longest_length

