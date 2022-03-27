class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False



obj1 = Solution()
print(obj1.isPalindrome(12111))
