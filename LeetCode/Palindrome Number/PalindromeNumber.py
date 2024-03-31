class Solution:
    def listToString(self, s: string) -> string:
 
    # initialize an empty string
        str1 = ""
 
    # traverse in the string
        for ele in s:
            str1 += ele
 
    # return string
        return str1
    def isPalindrome(self, x: int) -> bool:
        test = str(x)
        test1 = test[::-1]
        if test == test1:
            return True
        else:
            return False
