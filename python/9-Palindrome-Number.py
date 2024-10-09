class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_string = str(x)
        size = len(num_string)
        reversed_num = num_string[size::-1]

        if (str(x) != reversed_num):
            return False
        return True
