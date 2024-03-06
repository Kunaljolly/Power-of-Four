class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        x = 4
        while(x<=n):
            if x == n:
                return True
            x *= 4
        return False
        
