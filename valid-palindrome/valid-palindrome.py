class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(e for e in s if e.isalnum())
        reverse = ''.join(reversed(s))
        if (s == reverse):
            return True
        return False
# remove all punctuation 
# remove all spaces
# # sort and compare to the reverse