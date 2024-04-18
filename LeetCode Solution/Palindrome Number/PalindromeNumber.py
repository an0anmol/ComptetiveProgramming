class Solution:
    def isPalindrome(self, x: int) -> bool:
        test = str(x)
        test1 = test[::-1]
        if test == test1:
            return True
        else:
            return False
