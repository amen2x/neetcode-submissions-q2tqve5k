class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        
        new_s=""
        for i in s:
            if i.isalnum():
                new_s=new_s+i
        new_length=len(new_s)
        for i in range(new_length):
            if (new_s[i])!=(new_s[len(new_s)-1-i]):
                return False
        return True

        